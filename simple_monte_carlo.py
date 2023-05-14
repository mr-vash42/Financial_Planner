import unittest


class MonteCarloSimulation:
    def __init__(self, rates_of_return: list[float], starting_money: float, expenses: list[float]):
        self.rates_of_return = rates_of_return
        self.current_money = starting_money
        self.expenses = expenses

    def run(self) -> None:
        for rate_of_return, expense in zip(self.rates_of_return, self.expenses):
            self.current_money = self.current_money - expense
            self.current_money = (rate_of_return + 1) * self.current_money


class MyTestCase(unittest.TestCase):

    def assert_simulation_result(self, expected_ending_money: float, starting_money: float, per_period_info: dict[str, list[float]]) -> None:
        sim = MonteCarloSimulation(per_period_info['rates_of_return'], starting_money,
                                   per_period_info['expenses'])
        sim.run()
        self.assertEqual(sim.current_money, expected_ending_money)

    def test_one_period(self) -> None:
        per_period_info = {'rates_of_return': [.1], 'expenses': [0.0]}
        self.assert_simulation_result(1.1, starting_money=1, per_period_info=per_period_info)

    def test_two_periods(self) -> None:
        per_period_info = {'rates_of_return': [.1, .2], 'expenses': [0.0, 0.0]}
        self.assert_simulation_result(1.32, starting_money=1, per_period_info=per_period_info)

    def test_two_periods_adding_expenses(self) -> None:
        per_period_info = {'rates_of_return': [.01, .01], 'expenses': [5000.0, 5000.0]}
        self.assert_simulation_result(1009949.50, starting_money=1000000, per_period_info=per_period_info)


if __name__ == '__main__':
    unittest.main()
