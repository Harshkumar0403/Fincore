from ddgs import DDGS


def web_search(query: str, max_results: int = 5):

    with DDGS() as ddgs:

        results = list(
            ddgs.text(
                query,
                max_results=max_results
            )
        )

    return {
        "tool": "web_search",
        "results": results
    }


if __name__ == "__main__":

    print(
        web_search(
            "latest apple earnings"
        )
    )
