from unittest import TestCase
from ..build import cor
from inspect import getfullargspec
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')


class TestLoad_cor(TestCase):
    def test_cor_arguments(self):
        # Input parameters tests
        args = getfullargspec(cor)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))

    def test_cor_defaults(self):
        args = getfullargspec(cor)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")
