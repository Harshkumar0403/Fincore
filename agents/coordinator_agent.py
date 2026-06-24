from pathlib import Path
import json
import re

from agno.agent import Agent

from config.models import judge_model


COORDINATOR_PROMPT = Path(
    "prompts/coordinator_prompt.txt"
).read_text()


coordinator_agent = Agent(
    model=judge_model,
    instructions=COORDINATOR_PROMPT,
    markdown=False
)


def determine_tools(query: str):

    response = coordinator_agent.run(
        f"User Query:\n{query}"
    )

    raw_output = response.content.strip()

    # remove accidental markdown fences
    raw_output = re.sub(r"```json", "", raw_output)
    raw_output = re.sub(r"```", "", raw_output)
    raw_output = raw_output.strip()

    return json.loads(raw_output)
