import unittest
import numpy


class MonteCarloSimulation:
    def __init__(self, rates_of_return: list[float], starting_money: float, expenses: list[float], incomes: list[float]):
        self.rates_of_return = rates_of_return
        self.current_money = starting_money
        self.expenses = expenses
        self.incomes = incomes

    def run(self) -> None:
        for rate_of_return, expense, income in zip(self.rates_of_return, self.expenses, self.incomes):
            self.current_money = self.current_money - expense + income
            self.current_money = (rate_of_return + 1) * self.current_money


class SimulationTests(unittest.TestCase):

    def assert_simulation_result(self, expected_ending_money: float, starting_money: float, per_period_info: dict[str, list[float]]) -> None:
        if 'incomes' in per_period_info:
            incomes = per_period_info['incomes']
        else:
            incomes = list(numpy.zeros(len(per_period_info['rates_of_return'])))

        if 'expenses' in per_period_info:
            expenses = per_period_info['expenses']
        else:
            expenses = list(numpy.zeros(len(per_period_info['rates_of_return'])))

        sim = MonteCarloSimulation(per_period_info['rates_of_return'], starting_money,
                                   expenses, incomes)
        sim.run()
        self.assertEqual(sim.current_money, expected_ending_money)

    def test_one_period(self) -> None:
        per_period_info = {'rates_of_return': [.1]}
        self.assert_simulation_result(1.1, starting_money=1, per_period_info=per_period_info)

    def test_two_periods(self) -> None:
        per_period_info = {'rates_of_return': [.1, .2]}
        self.assert_simulation_result(1.32, starting_money=1, per_period_info=per_period_info)

    def test_two_periods_adding_expenses(self) -> None:
        per_period_info = {'rates_of_return': [.01, .01], 'expenses': [5000.0, 5000.0]}
        self.assert_simulation_result(1009949.50, starting_money=1000000, per_period_info=per_period_info)

    def test_two_periods_adding_income(self) -> None:
        per_period_info = {'rates_of_return': [.01, .01], 'expenses': [5000.0, 5000.0], 'incomes': [1000.0, 1000.0]}
        self.assert_simulation_result(1011979.6, starting_money=1000000, per_period_info=per_period_info)


if __name__ == '__main__':
    unittest.main()
