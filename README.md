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
- Frontend: HTML, CSS, JavaScript  
- Backend: Python (Flask / FastAPI)  
- Data Handling: Pandas  
- Embeddings: Sentence Transformers  
- Vector Database: FAISS  
- LLM: Groq API  

## 🔄 Workflow
1. Prepare Data  
2. Chunk Data  
3. Create Embeddings  
4. Store in FAISS  
5. User Query  
6. Retrieval  
7. AI Processing  
8. Final Output  

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
