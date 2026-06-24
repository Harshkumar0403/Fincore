from agno.models.groq import Groq

from config.settings import (
    GROQ_API_KEY,
    MAIN_MODEL,
    JUDGE_MODEL
)


main_llm = Groq(
    id=MAIN_MODEL,
    api_key=GROQ_API_KEY
)


judge_llm = Groq(
    id=JUDGE_MODEL,
    api_key=GROQ_API_KEY

)

main_model = Groq(
    id=MAIN_MODEL,
    api_key=GROQ_API_KEY
)

judge_model = Groq(
    id=JUDGE_MODEL,
    api_key=GROQ_API_KEY
)
