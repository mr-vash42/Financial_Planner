import unittest


class Taxes:
    def __init__(self, flat_tax):
        self.flat_tax = flat_tax

    def get_total_tax(self, gross):
        return self.flat_tax

    def get_income_net_of_taxes(self, gross):
        return gross - self.get_total_tax(gross)


class TestTaxes(unittest.TestCase):
    def test_fixed_cost_tax(self):
        taxes = Taxes(flat_tax=100)
        gross_income = 1000.
        self.assertEqual(100., taxes.get_total_tax(gross_income))
        self.assertEqual(900., taxes.get_income_net_of_taxes(gross_income))


if __name__ == '__main__':
    unittest.main()
