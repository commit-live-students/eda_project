from unittest import TestCase
from ..build import regression_plot
from inspect import getargspec
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')


class TestLoad_regression_plot(TestCase):
    def test_regression_plot(self):
        # Input parameters tests
        args = getargspec(regression_plot)
        self.assertEqual(len(args[0]), 2, "Expected arguments %d, Given %d" % (2, len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        regression_plot('GrLivArea', 'SalePrice')
        self.assertTrue(True)
