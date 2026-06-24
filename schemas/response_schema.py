from pydantic import BaseModel
from typing import List, Dict, Any

from schemas.judge_schema import JudgeFeedback


class FinalResponse(BaseModel):

    query: str

    tools_used: List[str]

    reasoning: str

    research_summary: str

    final_answer: str

    judge_feedback: JudgeFeedback

    processing_time: float

    metadata: Dict[str, Any]
