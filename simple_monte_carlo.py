import unittest


class MonteCarloSimulation:
    def __init__(self, rates_of_return: list[float], starting_money: float, expenses: float):
        self.rates_of_return = rates_of_return
        self.current_money = starting_money

    def run(self) -> None:
        for rate_of_return in self.rates_of_return:
            self.current_money = (rate_of_return + 1) * self.current_money


class MyTestCase(unittest.TestCase):
    def test_one_period(self) -> None:
        sim = MonteCarloSimulation(rates_of_return=[.1], starting_money=1, expenses=[0])
        sim.run()
        self.assertEqual(sim.current_money, 1.1)

    def test_two_periods(self) -> None:
        sim = MonteCarloSimulation(rates_of_return=[.1, .2], starting_money=1, expenses=[0, 0])
        sim.run()
        self.assertEqual(sim.current_money, 1.32)

    def test_two_periods_adding_expenses(self) -> None:
        sim = MonteCarloSimulation(rates_of_return=[.01, .01], starting_money=1000000, expenses=[5000, 5000])
        sim.run()
        self.assertAlmostEqual(sim.current_money, 1009950)


if __name__ == '__main__':
    unittest.main()
