import argparse
import time

from agents.coordinator_agent import determine_tools
from agents.research_agent import generate_research_summary
from agents.analysis_agent import generate_final_answer
from agents.judge_agent import evaluate_response

from schemas.response_schema import FinalResponse

from utils.ticker_extractor import extract_ticker

from tools.rag_tool import rag_search
from tools.ddgs_tool import web_search
from tools.calculator_tool import percentage_change

from tools.yfinance_tool import (
    get_stock_data,
    get_weekly_prices
)


def execute_tools(query: str, selected_tools: list):

    metadata = {}

    #
    # RAG
    #
    if "rag" in selected_tools:

        metadata["rag_results"] = rag_search(query)

    #
    # WEB SEARCH
    #
    if "web" in selected_tools:

        metadata["web_results"] = web_search(query)

    #
    # YFINANCE
    #
    if "yfinance" in selected_tools:

        ticker = extract_ticker(query)

        if ticker:

            metadata["stock_data"] = get_stock_data(ticker)

            #
            # Weekly change support
            #
            if "week" in query.lower():

                prices = get_weekly_prices(ticker)

                if prices:

                    pct_change = percentage_change(
                        prices["previous_close"],
                        prices["current_price"]
                    )

                    metadata["weekly_change"] = {

                        "ticker": ticker,

                        "previous_close":
                            prices["previous_close"],

                        "current_price":
                            prices["current_price"],

                        "percentage_change":
                            pct_change
                    }

        else:

            metadata["stock_data"] = {
                "error": "No ticker detected."
            }

    return metadata


def run_pipeline(query: str):

    start_time = time.time()

    #
    # Coordinator
    #
    coordinator_output = determine_tools(query)

    tools_used = coordinator_output["tools"]

    reasoning = coordinator_output["reasoning"]

    #
    # Execute tools
    #
    metadata = execute_tools(
        query=query,
        selected_tools=tools_used
    ) or {}

    #
    # Research Agent
    #
    research_summary = generate_research_summary(
        query=query,
        context=metadata
    )

    #
    # Analysis Agent
    #
    final_answer = generate_final_answer(
        query=query,
        research_summary=research_summary
    )

    #
    # Judge Agent
    #
    judge_feedback = evaluate_response(
        query=query,
        research_summary=research_summary,
        final_answer=final_answer
    )

    #
    # Processing time
    #
    elapsed_time = round(
        time.time() - start_time,
        2
    )

    #
    # Final response
    #
    response = FinalResponse(

        query=query,

        tools_used=tools_used,

        reasoning=reasoning,

        research_summary=research_summary,

        final_answer=final_answer,

        judge_feedback=judge_feedback,

        processing_time=elapsed_time,

        metadata=metadata
    )

    return response


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--query",
        type=str,
        required=True
    )

    args = parser.parse_args()

    response = run_pipeline(args.query)

    print(
        response.model_dump_json(
            indent=2
        )
    )
