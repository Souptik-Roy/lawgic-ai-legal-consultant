# This code takes legal data from a CSV file and turns each row into a simple text paragraph.
# Then it converts each paragraph into numbers (vectors) using an AI model.
# These numbers represent the meaning of the text, so similar meanings will have similar numbers.
# This helps in searching the correct law based on user questions, even if the words are different.
# This is the basic step for building a smart legal chatbot (RAG system).




from wsgiref import types

import pandas as pd

df = pd.read_csv("C:\\Users\\soupt\\OneDrive\\Desktop\\project-v\\lawgic-ai-legal-consultant\\data\\Law Sheet - Sheet1.csv")

# Step 1: Load Excel dataset and convert each row into a single readable paragraph list

def combine_row(row):
    parts = []
    for col in df.columns:
        val = str(row[col]).strip()
        if val and val != "nan":
            parts.append(f"{col}: {val}")
    return "\n".join(parts)

df["combined"] = df.apply(combine_row, axis=1)

texts = df["combined"].tolist()
# print(texts[0])




#Step 2: Convert text paragraphs into vectors (embeddings) using a pre-trained model

from sentence_transformers import SentenceTransformer

# Load model (lightweight, good enough for your project)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert your text list → embeddings
embeddings = model.encode(texts, show_progress_bar=True)

# # Check
# print(len(embeddings))        # should match number of rows
# print(embeddings[0].shape)   # vector size (usually 384)


#step 3: Build a FAISS index to store and search these vectors efficiently
import faiss
import numpy as np

# Convert embeddings to numpy array
embedding_array = np.array(embeddings).astype('float32')

# Get dimension (384)
dimension = embedding_array.shape[1]

# Create FAISS index
index = faiss.IndexFlatL2(dimension)

# Add all embeddings to index
index.add(embedding_array)

#step 4: Search the index with a user query to find relevant legal information

query = input("Enter your legal question: ")

# Convert query → embedding
query_vector = model.encode([query]).astype('float32')

# Search top 3 similar texts
D, I = index.search(query_vector, k=3)

# Get results
# results = [texts[i] for i in I[0]]

# Step 4: Extract only the "Effect" from each section
effects = []
for i in I[0]:
    text = texts[i]
    # Assuming "Effect:" starts the effect section
    if "Effect:" in text:
        part = text.split("Effect:")[1].strip()
        effects.append(part)

# Merge all effects into one string
merged_effects = " ".join(effects)


# for r in results:
#     print(r)
#     print("------")
    
 #step 5: Use the retrieved legal context to answer the user's question (RAG)   
context = "\n\n".join(merged_effects)
# Assume `merged_effects` contains only the Effect parts from top relevant sections

prompt = f"""
You are a professional legal consultant.

Using only the legal effects provided below, give a clear and concise answer to the client's question.
- Do not include sections, causes, explanations, or URLs.
- Merge the effects into a simple, understandable legal advice.

Legal Effects:
{merged_effects}

Client Question:
{query}

Legal Advice (Effect only):
"""

#step 6: Generate the final answer using a language model (like Gemini or GPT-4)
from transformers import pipeline

# Load a small GPT model (runs on CPU)
generator = pipeline("text-generation", model="gpt2")

output = generator(prompt, max_length=500, do_sample=True, temperature=0.7)

print(output[0]['generated_text'])