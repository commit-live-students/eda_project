from unittest import TestCase
from q04_cor.build import cor

class TestLoad_cor(TestCase):
    def test_cor(self):
        cor('GrLivArea', 'SalePrice')
        self.assertTrue(True)