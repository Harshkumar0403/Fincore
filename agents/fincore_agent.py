from app import run_pipeline


def ask_fincore(query: str) -> str:
    """
    Entry point for Agno UI.
    Executes the complete FinCore pipeline.
    """

    response = run_pipeline(query)

    output = f"""
Question:
{response.query}

Answer:
{response.final_answer}

Tools Used:
{", ".join(response.tools_used)}

Confidence Score:
{response.judge_feedback.overall_score}

Processing Time:
{response.processing_time} seconds
"""

    return output.strip()
