from unittest import TestCase
from q03_regression_plot.build import regression_plot

class TestLoad_regression_plot(TestCase):
    def test_regression_plot(self):
        regression_plot('GrLivArea', 'SalePrice')
        self.assertTrue(True)