from unittest import TestCase
from ..build import cor
from inspect import getargspec
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')


class TestLoad_cor(TestCase):
    def test_cor(self):
        # Input parameters tests
        args = getargspec(cor)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")