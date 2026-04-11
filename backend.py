from fastapi  import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Query(BaseModel):
    query:str

#actual answering logic will be implemented here
def rag_pipeline(query:str):
    return f"Response for query: {query}"


#actual endpoint to handle the query and return the response
@app.post("/query")
def handle_query(query:Query):
    response=rag_pipeline(query.query)
    return {"response": response}