import unittest


class MonteCarloSimulation:
    def __init__(self, rates_of_return: list[float], starting_money: float):
        self.rates_of_return = rates_of_return
        self.current_money = starting_money

    def run(self) -> None:
        for rate_of_return in self.rates_of_return:
            self.current_money = (rate_of_return + 1) * self.current_money


class MyTestCase(unittest.TestCase):
    def test_one_period(self) -> None:
        sim = MonteCarloSimulation(rates_of_return=[.1], starting_money=1)
        sim.run()
        self.assertEqual(sim.current_money, 1.1)

    def test_two_periods(self) -> None:
        sim = MonteCarloSimulation(rates_of_return=[.1, .2], starting_money=1)
        sim.run()
        self.assertEqual(sim.current_money, 1.32)


if __name__ == '__main__':
    unittest.main()
