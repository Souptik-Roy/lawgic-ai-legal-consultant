from fastapi  import FastAPI
from pydantic import BaseModel
from rag import rag_pipeline

app=FastAPI()

class Query(BaseModel):
    query:str
#actual endpoint to handle the query and return the response
@app.post("/query")
def handle_query(query:Query):
    answer=rag_pipeline(query.query)
    return {"Responses from LawGic\n": answer}