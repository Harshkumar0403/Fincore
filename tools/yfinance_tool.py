import yfinance as yf

def get_stock_data(ticker: str):

    ticker = ticker.upper()

    stock = yf.Ticker(ticker)

    info = stock.info

    return {

        "ticker": ticker,

        "current_price":
            info.get("currentPrice"),

        "market_cap":
            info.get("marketCap"),

        "pe_ratio":
            info.get("trailingPE"),

        "forward_pe":
            info.get("forwardPE"),

        "volume":
            info.get("volume"),

        "average_volume":
            info.get("averageVolume"),

        "fifty_two_week_high":
            info.get("fiftyTwoWeekHigh"),

        "fifty_two_week_low":
            info.get("fiftyTwoWeekLow"),

        "dividend_yield":
            info.get("dividendYield"),

        "sector":
            info.get("sector"),

        "industry":
            info.get("industry")
    }


def get_price_history(
        ticker: str,
        period: str = "1mo"
):

    ticker = ticker.upper()

    stock = yf.Ticker(ticker)

    history = stock.history(period=period)

    return history


def get_weekly_prices(ticker: str):

    ticker = ticker.upper()

    stock = yf.Ticker(ticker)

    history = stock.history(period="7d")

    if len(history) < 2:

        return None

    return {

        "ticker": ticker,

        "previous_close":
            round(float(history["Close"].iloc[0]), 2),

        "current_price":
            round(float(history["Close"].iloc[-1]), 2)
    }


def get_options_data(ticker: str):

    ticker = ticker.upper()

    stock = yf.Ticker(ticker)

    expirations = stock.options

    if not expirations:

        return {
            "ticker": ticker,
            "error": "No options data available"
        }

    nearest_expiry = expirations[0]

    option_chain = stock.option_chain(nearest_expiry)

    calls = option_chain.calls

    puts = option_chain.puts

    call_volume = int(calls["volume"].fillna(0).sum())

    put_volume = int(puts["volume"].fillna(0).sum())

    put_call_ratio = (
        round(put_volume / call_volume, 3)
        if call_volume > 0
        else None
    )

    return {

        "ticker": ticker,

        "expiration":
            nearest_expiry,

        "call_volume":
            call_volume,

        "put_volume":
            put_volume,

        "put_call_ratio":
            put_call_ratio
    }


if __name__ == "__main__":

    print("\n=== BASIC DATA ===")
    print(get_stock_data("AAPL"))

    print("\n=== WEEKLY CHANGE ===")
    print(calculate_weekly_change("AAPL"))

    print("\n=== OPTIONS DATA ===")
    print(get_options_data("AAPL"))
