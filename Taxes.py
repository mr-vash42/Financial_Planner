import unittest


class Taxes:
    def __init__(self, taxes) -> None:
        self.taxes = taxes

    def get_total_tax(self, gross_income: float) -> float:
        return sum([tax.get_tax_contribution(gross_income) for tax in self.taxes])

    def get_income_net_of_taxes(self, gross: float) -> float:
        return gross - self.get_total_tax(gross)


class FixedTax:
    def __init__(self, fixed_tax):
        self.tax = fixed_tax

    def get_tax_contribution(self, gross_income=0) -> float:
        return self.tax


class FlatRateTax:
    def __init__(self, tax_rate):
        self.tax = tax_rate

    def get_tax_contribution(self, gross_income=0) -> float:
        return self.tax*gross_income


class GraduatedRatesTax:
    def __init__(self, tax_rates, terminal_tax_rate):
        self.tax_rates = tax_rates
        self.terminal_tax_rate = terminal_tax_rate

    def get_tax_contribution(self, gross_income=0) -> float:
        cumulative_grad_taxes = 0
        remaining_dollars_to_be_taxed = gross_income
        for dollars_in_bracket, rate in zip(self.tax_rates.keys(), self.tax_rates.values()):
            if dollars_in_bracket < remaining_dollars_to_be_taxed:
                cumulative_grad_taxes += dollars_in_bracket * rate
                remaining_dollars_to_be_taxed -= dollars_in_bracket
            else:
                return cumulative_grad_taxes + remaining_dollars_to_be_taxed * rate
        return cumulative_grad_taxes + self.terminal_tax_rate * remaining_dollars_to_be_taxed


class TestTaxes(unittest.TestCase):
    def test_fixed_cost_tax(self):
        taxes = Taxes([FixedTax(100)])
        self.assertEqual(100., taxes.get_total_tax(1000.))
        self.assertEqual(900., taxes.get_income_net_of_taxes(1000.))

    def test_flat_rate_tax(self):
        taxes = Taxes([FlatRateTax(.15)])
        self.assertEqual(150, taxes.get_total_tax(1000))
        self.assertEqual(300, taxes.get_total_tax(2000))
        self.assertEqual(4250, taxes.get_income_net_of_taxes(5000))

    def test_graduated_tax_rate(self):
        taxes = Taxes([GraduatedRatesTax(tax_rates={50000: 0, 20000: .10}, terminal_tax_rate=.20)])
        self.assertEqual(0, taxes.get_total_tax(50000))
        self.assertEqual(1000, taxes.get_total_tax(60000))
        self.assertEqual(4000, taxes.get_total_tax(80000))

    def test_2023_federal_tax_married_rates(self):
        taxes = Taxes([GraduatedRatesTax(terminal_tax_rate=.37, tax_rates={22000: .1,
                                                                           67450: .12,
                                                                           101300: .22,
                                                                           173450: .24,
                                                                           98300: .32,
                                                                           231250: .35
                                                                           }
                                         )
                       ]
                      )
        self.assertEqual(10294., taxes.get_total_tax(89450))
        self.assertEqual(74208. + (.32 * 10000), taxes.get_total_tax(364200 + 10000))
        self.assertEqual(299914., taxes.get_total_tax(10**6))

    def test_all_taxes_together(self):
        taxes = Taxes([FixedTax(100), FlatRateTax(.10), GraduatedRatesTax({2000: 0, 40000: .20}, .25)])
        self.assertEqual(100 + 8000 + 0 + 8000 + 9500, taxes.get_total_tax(80000.))


if __name__ == '__main__':
    unittest.main()
