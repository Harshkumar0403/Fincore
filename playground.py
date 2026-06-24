from agno.agent import Agent
from agno.playground import Playground
from agno.models.groq import Groq

from agents.fincore_agent import ask_fincore


fincore_agent = Agent(
    name="FinCore AI",
    role="Financial Research Assistant",

    model=Groq(
        id="openai/gpt-oss-120b"
    ),

    instructions="""
You are FinCore AI.

Your responsibility is to answer finance and accounting questions.

Always use the FinCore backend pipeline.

Provide professional responses.
""",

    tools=[ask_fincore],

    markdown=True
)


playground = Playground(
    agents=[fincore_agent]
)

app = playground.get_app()
