from agents.research_agent import generate_research_summary


context = {
    "rag_results": [
        {
            "text": "Working capital is current assets minus current liabilities."
        }
    ]
}


output = generate_research_summary(
    query="What is working capital?",
    context=context
)

print(output)
