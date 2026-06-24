from fastapi import FastAPI
from pydantic import BaseModel

from app import run_pipeline


app = FastAPI(
    title="FinCore AI",
    description="Agentic Financial Research Assistant",
    version="1.0"
)


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():

    return {
        "message": "FinCore AI API is running."
    }


@app.post("/query")
def query_finance(request: QueryRequest):

    response = run_pipeline(
        request.query
    )

    return response.model_dump()
