import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from google import genai
import os
# ==============================
# GEMINI SETUP (ONCE)
# ==============================

from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
# print(api_key)  # to check that api key is loaded

client = genai.Client(api_key=api_key)
# LOAD DATA (ONCE)
# ==============================
df = pd.read_csv("C:\\Users\\soupt\\OneDrive\\Desktop\\project-v\\lawgic-ai-legal-consultant\\data\\Law Sheet - Sheet1.csv")  

def combine_row(row):
    parts = []
    for col in df.columns:
        val = str(row[col]).strip()
        if val and val != "nan":
            parts.append(f"{col}: {val}")
    return "\n".join(parts)

df["combined"] = df.apply(combine_row, axis=1)
texts = df["combined"].tolist()

# ==============================
# EMBEDDING + INDEX (ONCE)
# ==============================
model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode(texts)
embedding_array = np.array(embeddings).astype('float32')

dimension = embedding_array.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embedding_array)


# ==============================
# MAIN RAG FUNCTION
# ==============================
def rag_pipeline(query):

    # STEP 1: query → embedding
    query_vector = model.encode([query]).astype('float32')

    # STEP 2: search top 3
    D, I = index.search(query_vector, k=3)  # D: distances, I: indices

    retrieved_texts = [texts[i] for i in I[0]]

    # STEP 3: create prompt
    prompt = f"""
You are a legal advisor.

Read the legal information and answer in a simple, practical, and realistic way.

Your task:
- Combine all relevant laws into ONE section line
- Give ONE clear condition
- Give ONE practical legal outcome
- Add a short real-world note

Rules:
- Use ONLY the given legal information
- Keep language simple
- Merge sections using '+'
- If not found, say: "No relevant law found"

------------------------------
Question:
{query}
------------------------------

Legal Information:
{retrieved_texts}

------------------------------
Answer Format:
------------------------------
Query:
Section:
Condition:
Punishment:
Practical Note:
"""

    # STEP 4: Gemini call
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text

# olama


