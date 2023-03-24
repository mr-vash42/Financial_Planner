import unittest


class MonteCarloSimulation:
    def __init__(self, rates_of_return: list[float], starting_money: float, expenses: list[float]):
        self.rates_of_return = rates_of_return
        self.current_money = starting_money

    def run(self) -> None:
        for rate_of_return in self.rates_of_return:
            self.current_money = (rate_of_return + 1) * self.current_money


class MyTestCase(unittest.TestCase):

    def assert_simulation_result(self, expected_ending_money, rates_of_return, starting_money, expenses) -> None:
        sim = MonteCarloSimulation(rates_of_return, starting_money, expenses)
        sim.run()
        self.assertEqual(sim.current_money, expected_ending_money)

    def test_one_period(self) -> None:
        self.assert_simulation_result(1.1, [.1], 1, [0])

    def test_two_periods(self) -> None:
        self.assert_simulation_result(1.32, [.1, .2], 1, [0, 0])

    def test_two_periods_adding_expenses(self) -> None:
        self.assert_simulation_result(1009950, [.01, .01], 1000000, [5000, 5000])



if __name__ == '__main__':
    unittest.main()
