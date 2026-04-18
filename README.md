# ⚖️ LAWGIC — LegalAnalytics Workflow using General Intelligence Consultancy 

## 📌 Project Overview 
LAWGIC is an AI-powered legal consultancy system designed to help common people understand legal issues in simple language.

Instead of reading complex law books, users can ask questions in natural language, and the system will:
- Find relevant legal information from a dataset
- Analyze it using AI
- Provide clear, structured, and easy-to-understand answers

## 🎯 Objective
To build a smart legal assistant that:
- Simplifies complex legal content  
- Provides quick legal guidance  
- Bridges the gap between law and common people  

## 🧠 Core Concept
This project uses:
**RAG (Retrieval-Augmented Generation)**

## ⚙️ Key Features
- Smart legal query understanding  
- Dataset-based answers (not random AI guesses)  
- Structured output (Explanation, Rights, Steps)  
- Chat-based interface  

## 🏗️ System Architecture
User → Frontend → Backend → Retrieval System → AI Model → Response

## 🧰 Tech Stack
- Data Handling: Pandas  
- Embeddings: Sentence Transformers  
- Vector Database: FAISS  
- LLM: Gemini API
- Backend: Python (FastAPI)  
- Frontend: HTML, CSS, JavaScript  
  

## 🔄 Workflow
1. Legal Data Collection (CSV dataset)
2. Data Cleaning & Row Structuring (combine_row → structured legal paragraphs)
3. Context-Aware Chunking (row-wise legal sections)
4. Embedding Generation (SentenceTransformer: all-MiniLM-L6-v2)
5. FAISS Index Creation & Storage (vector + text mapping)
6. API Initialization (FastAPI + load models once)
7. User Query Input (POST request via API)
8. Query Embedding (same embedding model)
9. Similarity Search (FAISS Top-K = 3 relevant laws)
10. Context Extraction (retrieve legal texts)
11. Prompt Engineering (structured legal reasoning format)
12. LLM Processing (Gemini generates legal advice)
13. Response Formatting (structured output: section, condition, punishment, note)
14. API Response Delivery (JSON output to client)
 

## 💡 Example
User: "My landlord is not returning my security deposit."

Output:
- Explanation of tenant rights  
- Legal steps  
- Practical guidance  

## 🧾 Final Simple Flow
User asks → System finds law → AI explains

## 🧠 Summary
LAWGIC = Search legal data + Explain using AI 
