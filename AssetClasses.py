import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def get_ticker_dividends(ticker_symbol: str) -> dict[pd.Timestamp, float]:
    ticker_obj = yf.Ticker(ticker_symbol)
    dividends_obj = ticker_obj.dividends
    # dividends.to_csv(f'{ticker_symbol}_dividends.csv')
    return dividends_obj.to_dict()


def plot_price_history(price_history: dict[pd.Timestamp, float]) -> None:

    df = pd.DataFrame(list(price_history.items()), columns=['Date', 'Price'])
    df.set_index('Date', inplace=True)

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Price'], marker='o', linestyle='-', color='b', label='Price')

    # Add titles and labels
    plt.title('Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Add grid
    plt.grid(True)

    # Add a legend
    plt.legend()

    # Show the plot
    plt.tight_layout()  # Adjust layout to make room for labels
    plt.show()


def main() -> None:
    price_history = get_ticker_price_history('VTSAX')['Adj Close']
    plot_price_history(price_history)
    #get_ticker_dividends('VTSAX')


def get_ticker_price_history(ticker_symbol: str) -> dict[str, dict[pd.Timestamp, float]]:
    ticker = ticker_symbol
    data = yf.download(ticker)
    return data.to_dict()

    # data.to_csv(f'historical {ticker} data')


if __name__ == '__main__':
    main()
