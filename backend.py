from fastapi  import FastAPI
from pydantic import BaseModel
from rag import rag_pipeline

app=FastAPI()

class Query(BaseModel):
    query:str
    
    
# @app.get("/")
# def read_root():    
#     return {"Server is running. Send a POST request to /query with your legal question."}
#actual endpoint to handle the query and return the response
@app.post("/query")
def handle_query(query:Query):
    answer=rag_pipeline(query.query)
    # answer = "This is a placeholder response. The RAG pipeline is currently under development."
    return {"Responses from LawGic\n": answer}