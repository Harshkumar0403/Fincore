import re


#
# Common company mappings
#
COMPANY_TO_TICKER = {

    "apple": "AAPL",

    "microsoft": "MSFT",

    "tesla": "TSLA",

    "nvidia": "NVDA",

    "amazon": "AMZN",

    "google": "GOOG",

    "alphabet": "GOOG",

    "meta": "META",

    "netflix": "NFLX",

    "amd": "AMD",

    "intel": "INTC",

    "oracle": "ORCL",

    "salesforce": "CRM"
}


def extract_ticker(query: str):

    #
    # Explicit ticker first
    #
    matches = re.findall(
        r"\b[A-Z]{1,5}\b",
        query
    )

    if matches:

        return matches[0]

    #
    # Company names
    #
    lower_query = query.lower()

    for company, ticker in COMPANY_TO_TICKER.items():

        if company in lower_query:

            return ticker

    return None
