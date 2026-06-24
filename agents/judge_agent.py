from pathlib import Path
import json
import re

from agno.agent import Agent

from config.models import judge_model
from schemas.judge_schema import JudgeFeedback


JUDGE_PROMPT = Path(
    "prompts/judge_prompt.txt"
).read_text()


judge_agent = Agent(
    model=judge_model,
    instructions=JUDGE_PROMPT,
    markdown=False
)


def evaluate_response(
    query: str,
    research_summary: str,
    final_answer: str
):

    prompt = f"""
User Query:
{query}

Research Findings:
{research_summary}

Analyst Response:
{final_answer}
"""

    response = judge_agent.run(prompt)

    raw_output = response.content.strip()

    # Remove markdown fences if present
    raw_output = re.sub(r"```json", "", raw_output)
    raw_output = re.sub(r"```", "", raw_output)
    raw_output = raw_output.strip()

    parsed = json.loads(raw_output)

    return JudgeFeedback(**parsed)
