from src.bun import Bun
from testing_data import TestingData
import pytest

class TestBun:
    @pytest.mark.parametrize('name, price',[
        (TestingData.BLACK_BUN_NAME, TestingData.BLACK_BUN_PRICE),
        (TestingData.WHITE_BUN_NAME, TestingData.WHITE_BUN_PRICE),
        (TestingData.RED_BUN_NAME, TestingData.RED_BUN_PRICE)
        ])
    
    def test_get_name_of_the_bun_name_got(self, bun, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
    
    @pytest.mark.parametrize('name, price',[
        (TestingData.BLACK_BUN_NAME, TestingData.BLACK_BUN_PRICE),
        (TestingData.WHITE_BUN_NAME, TestingData.WHITE_BUN_PRICE),
        (TestingData.RED_BUN_NAME, TestingData.RED_BUN_PRICE)
        ])
    def test_get_price_of_the_bun_price_got(self, bun, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price