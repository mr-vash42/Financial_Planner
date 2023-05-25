import unittest
from collections import OrderedDict


class Taxes:
    def __init__(self, flat_tax=0., flat_rate_tax=0., graduated_tax_rates=OrderedDict(), terminal_tax_rate=0.) -> None:
        self.flat_tax = flat_tax
        self.flat_rate_rate = flat_rate_tax
        self.graduated_tax_rates = graduated_tax_rates
        self.terminal_graduated_rate = terminal_tax_rate

    def get_total_tax(self, gross: float) -> float:
        return self.flat_tax + (gross * self.flat_rate_rate) + self.get_graduated_taxes(gross)

    def get_income_net_of_taxes(self, gross: float) -> float:
        return gross - self.get_total_tax(gross)

    def get_graduated_taxes(self, gross: float) -> float:
        cumulative_grad_taxes = 0
        remaining_dollars_to_be_taxed = gross
        for dollars_in_bracket, rate in zip(self.graduated_tax_rates.keys(), self.graduated_tax_rates.values()):
            if dollars_in_bracket < remaining_dollars_to_be_taxed:
                cumulative_grad_taxes += dollars_in_bracket*rate
                remaining_dollars_to_be_taxed -= dollars_in_bracket
            else:
                return cumulative_grad_taxes + remaining_dollars_to_be_taxed*rate
        return cumulative_grad_taxes + self.terminal_graduated_rate * remaining_dollars_to_be_taxed


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

    def test_graduated_tax_rate(self):
        taxes = Taxes(graduated_tax_rates=OrderedDict([(50000, 0), (20000, .10)]), terminal_tax_rate=.20)
        self.assertEqual(0, taxes.get_total_tax(50000))
        self.assertEqual(1000, taxes.get_total_tax(60000))
        self.assertEqual(4000, taxes.get_total_tax(80000))

    def test_2023_federal_tax_married_rates(self):
        taxes = Taxes(terminal_tax_rate=.37, graduated_tax_rates=OrderedDict([(22000, .1),
                                                                              (67450, .12),
                                                                              (101300, .22),
                                                                              (173450, .24),
                                                                              (98300, .32),
                                                                              (231250, .35),
                                                                              ]))
        self.assertEqual(10294., taxes.get_total_tax(89450))
        self.assertEqual(74208. + (.32 * 10000), taxes.get_total_tax(364200 + 10000))
        self.assertEqual(299914., taxes.get_total_tax(10**6))

    def test_all_taxes_together(self):
        taxes = Taxes(100, .10, OrderedDict([(2000, 0), (40000, .20)]), .25)
        self.assertEqual(100 + 8000 + 0 + 8000 + 9500, taxes.get_total_tax(80000.))


if __name__ == '__main__':
    unittest.main()
