from agents.analysis_agent import generate_final_answer


research_summary = """
Working capital is the difference between current assets and current liabilities.
It is used to measure short-term liquidity.
"""

output = generate_final_answer(
    query="What is working capital?",
    research_summary=research_summary
)

print(output)
