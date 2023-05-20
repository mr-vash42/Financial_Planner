import unittest


class Taxes:
    def __init__(self, flat_tax=0., flat_rate_tax=0.):
        self.flat_tax = flat_tax
        self.flat_rate_rate = flat_rate_tax

    def get_total_tax(self, gross: float) -> float:
        return self.flat_tax + (gross * self.flat_rate_rate)

    def get_income_net_of_taxes(self, gross: float) -> float:
        return gross - self.get_total_tax(gross)


class TestTaxes(unittest.TestCase):
    def test_fixed_cost_tax(self):
        taxes = Taxes(flat_tax=100)
        self.assertEqual(100., taxes.get_total_tax(1000.))
        self.assertEqual(900., taxes.get_income_net_of_taxes(1000.))

    def test_flat_rate_tax(self):
        taxes = Taxes(flat_rate_tax=.15)
        self.assertEqual(150, taxes.get_total_tax(1000))
        self.assertEqual(300, taxes.get_total_tax(2000))
        self.assertEqual(4250, taxes.get_income_net_of_taxes(5000))


if __name__ == '__main__':
    unittest.main()
