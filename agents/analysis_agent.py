from pathlib import Path

from agno.agent import Agent

from config.models import main_model


ANALYSIS_PROMPT = Path(
    "prompts/analysis_prompt.txt"
).read_text()


analysis_agent = Agent(
    model=main_model,
    instructions=ANALYSIS_PROMPT,
    markdown=False
)


def generate_final_answer(
    query: str,
    research_summary: str
):

    prompt = f"""
User Query:
{query}

Research Findings:
{research_summary}
"""

    response = analysis_agent.run(prompt)

    return response.content
