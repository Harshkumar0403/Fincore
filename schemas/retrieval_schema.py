from pydantic import BaseModel


class RetrievedChunk(BaseModel):
    source: str
    page: int
    similarity: float
    text: str
