import unittest


class MonteCarloSimulation:
    def __init__(self, rate_of_return: float, starting_money: float):
        self.rate_of_return = rate_of_return
        self.current_money = starting_money

    def run(self) -> None:
        self.current_money = (self.rate_of_return+1)*self.current_money


class MyTestCase(unittest.TestCase):
    def test_one_period(self):
        sim = MonteCarloSimulation(rate_of_return=.1, starting_money=1)
        sim.run()
        self.assertEqual(sim.current_money, 1.1)


if __name__ == '__main__':
    unittest.main()
