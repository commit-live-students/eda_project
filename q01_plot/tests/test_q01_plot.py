from unittest import TestCase
from q01_plot.build import plot

class TestLoad_distplot(TestCase):
    def test_plot(self):
        plot(['LotArea', 'GarageArea', 'OpenPorchSF', 'SalePrice'])
        self.assertTrue(True)