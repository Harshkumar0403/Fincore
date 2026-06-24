from pathlib import Path

from agno.agent import Agent

from config.models import main_model


RESEARCH_PROMPT = Path(
    "prompts/research_prompt.txt"
).read_text()


research_agent = Agent(
    model=main_model,
    instructions=RESEARCH_PROMPT,
    markdown=False
)

def generate_research_summary(
    query: str,
    context: dict
):

    prompt = f"""
User Query:
{query}

Research Context:
{context}
"""

    response = research_agent.run(prompt)

    return response.content
