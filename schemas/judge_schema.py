from pydantic import BaseModel


class JudgeFeedback(BaseModel):
    factual_accuracy: int
    grammar_quality: int
    relevance: int
    overall_score: float
    strengths: str
    weaknesses: str
