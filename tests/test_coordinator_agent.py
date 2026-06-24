from agents.coordinator_agent import determine_tools


queries = [

    "What is working capital?",

    "Latest Apple earnings",

    "Current PE ratio of NVDA",

    "What is the percentage change of NVDA price from previous week?",

    "Explain depreciation and tell me whether Apple discussed it in recent earnings."
]


for q in queries:

    print("\n")
    print(q)

    output = determine_tools(q)

    print(output)
