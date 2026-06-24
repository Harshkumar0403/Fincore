from agents.judge_agent import evaluate_response


research_summary = """
Working capital = current assets - current liabilities.
"""

final_answer = """
Working capital is the difference between current assets and current liabilities.
"""

output = evaluate_response(
    query="What is working capital?",
    research_summary=research_summary,
    final_answer=final_answer
)

print(output)
