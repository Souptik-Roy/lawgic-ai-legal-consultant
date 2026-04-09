# # This code takes legal data from a CSV file and turns each row into a simple text paragraph.
# # Then it converts each paragraph into numbers (vectors) using an AI model.
# # These numbers represent the meaning of the text, so similar meanings will have similar numbers.
# # This helps in searching the correct law based on user questions, even if the words are different.
# # This is the basic step for building a smart legal chatbot (RAG system).




# from wsgiref import types

# import pandas as pd

# df = pd.read_csv("data/Law Sheet.csv")

# # Step 1: Load Excel dataset and convert each row into a single readable paragraph list

# def combine_row(row):
#     parts = []
#     for col in df.columns:
#         val = str(row[col]).strip()
#         if val and val != "nan":
#             parts.append(f"{col}: {val}")
#     return "\n".join(parts)

# df["combined"] = df.apply(combine_row, axis=1)

# texts = df["combined"].tolist()
# # print(texts[0])




# #Step 2: Convert text paragraphs into vectors (embeddings) using a pre-trained model

# from sentence_transformers import SentenceTransformer

# # Load model (lightweight, good enough for your project)
# model = SentenceTransformer('all-MiniLM-L6-v2')

# # Convert your text list → embeddings
# embeddings = model.encode(texts, show_progress_bar=True)

# # # Check
# # print(len(embeddings))        # should match number of rows
# # print(embeddings[0].shape)   # vector size (usually 384)


# #step 3: Build a FAISS index to store and search these vectors efficiently
# import faiss
# import numpy as np

# # Convert embeddings to numpy array
# embedding_array = np.array(embeddings).astype('float32')

# # Get dimension (384)
# dimension = embedding_array.shape[1]

# # Create FAISS index
# index = faiss.IndexFlatL2(dimension)

# # Add all embeddings to index
# index.add(embedding_array)

# #step 4: Search the index with a user query to find relevant legal information

# query = "someone cheated me online"

# # Convert query → embedding
# query_vector = model.encode([query]).astype('float32')

# # Search top 3 similar texts
# D, I = index.search(query_vector, k=3)

# # Get results
# results = [texts[i] for i in I[0]]

# # for r in results:
# #     print(r)
# #     print("------")
    
#  #step 5: Use the retrieved legal context to answer the user's question (RAG)   
# context = "\n\n".join(results)

# prompt_name = f"""
# You are a legal consultant assisting a client.

# Based on the legal information provided below, answer the question in a clear and professional way.

# Guidelines:
# - Use only the given legal context
# - Explain in simple language, as if advising a client
# - Mention relevant Sections or Acts where applicable
# - If multiple laws apply, explain them briefly and clearly
# - Do not guess or add information not present in the context
# - If the answer is not available, say: "I could not find a relevant law in the provided data"

# Legal Context:
# {context}

# Client Question:
# {query}

# Legal Advice:
# """

#step 6: Generate the final answer using a language model (like Gemini or GPT-4)
from google import genai
# from google.genai import types
# from google.generativeai import Client

# import os

# ✅ Set your API key (replace with your actual key)
# os.environ["GOOGLE_API_KEY"] = "AIzaSyCRLcYfScrmpUKgKY19xZtx_3ZUyWlvvbg"

# Create a Gemini client
# client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
client = genai.Client(api_key="AIzaSyCRLcYfScrmpUKgKY19xZtx_3ZUyWlvvbg")

# Choose the model
model_name = "models/gemini-2.5-flash"
# from google.ai.generativelanguage import types, models
from google.genai import types
prompt_text = "What is the capital of France?"

# assume prompt_name is already defined as a string
part = types.Part.from_text(prompt_text)  # only one argument

response = client.generate_content(
    model=model_name,
    # model="gemini-2.5-flash",
    contents=part,
    config=types.GenerateContentConfig(
        temperature=0,
        top_p=0.95,
        top_k=20,
    ),
)

# print the text from the response
print(response.result[0].content[0].text)