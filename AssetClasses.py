import unittest
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import statistics


class Tickers:
    US_EQUITY = 'VTSAX'
    NON_US_DEVELOPED_EQUITY = 'VTMGX'
    EMERGING_MARKETS_EQUITY = 'VEMAX'


def get_price_change_history(monthly_price_history: list[float]) -> list[float]:
    changes = []
    for i in range(1, len(monthly_price_history)):
        prev_price = monthly_price_history[i - 1]
        curr_price = monthly_price_history[i]

        if prev_price == 0:
            change = float('inf')
        else:
            change = ((curr_price - prev_price) / prev_price) * 100

        changes.append(change)

    return changes


def main() -> None:
    monthly_price_history = get_adjusted_price_history('VTSAX')
    price_change_history = get_price_change_history(list(monthly_price_history.values()))
    aretmatic_mean_monthly_return = statistics.mean(price_change_history)
    monthly_standard_dev = statistics.stdev(price_change_history)
    pass


def get_adjusted_price_history(ticker: str) -> dict[datetime.date, float]:
    data = yf.download(ticker, interval='1mo')
    return {timestamp.date(): value for timestamp, value in data.to_dict()['Adj Close'].items()}


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


if __name__ == '__main__':
    main()


class TestGetPriceChangeHistory(unittest.TestCase):

    def assertListAlmostEqual(self, list1, list2, places=7):
        self.assertEqual(len(list1), len(list2), "Lists are of different lengths.")
        for a, b in zip(list1, list2):
            self.assertAlmostEqual(a, b, places=places)

    def test_one_change(self):
        prices = [100.0, 110.0]
        expected_changes = [10.0]
        self.assertAlmostEqual(get_price_change_history(prices), expected_changes, places=6)

    def test_normal_case(self):
        prices = [100.0, 110.0, 105.0, 115.0]
        expected_changes = [10.0, -4.545454545454546, 9.523809523809524]
        self.assertAlmostEqual(get_price_change_history(prices), expected_changes, places=6)

    def test_zero_price(self):
        prices = [0.0, 100.0]
        expected_changes = [float('inf')]  # Infinite change due to division by zero
        self.assertEqual(get_price_change_history(prices), expected_changes)

    def test_single_entry(self):
        prices = [100.0]
        expected_changes = []
        self.assertEqual(get_price_change_history(prices), expected_changes)

    def test_empty_list(self):
        prices = []
        expected_changes = []
        self.assertEqual(get_price_change_history(prices), expected_changes)

    def test_decreasing_prices(self):
        prices = [150.0, 130.0, 120.0, 110.0]
        expected_changes = [-13.333333333333334, -7.6923076923076925, -8.333333333333334]
        self.assertListAlmostEqual(get_price_change_history(prices), expected_changes, places=6)

    def test_constant_prices(self):
        prices = [100.0, 100.0, 100.0, 100.0]
        expected_changes = [0.0, 0.0, 0.0]
        self.assertEqual(get_price_change_history(prices), expected_changes)

    def test_large_numbers(self):
        prices = [1e6, 1.2e6, 1.5e6]
        expected_changes = [20.0, 25.0]
        self.assertAlmostEqual(get_price_change_history(prices), expected_changes, places=6)