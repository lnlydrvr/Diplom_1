import pytest
from tests.testing_data import TestingData
from src.bun import Bun

@pytest.fixture(scope='function')
def bun():
    test_bun = Bun(TestingData.BLACK_BUN_NAME, TestingData.BLACK_BUN_PRICE)
    return test_bun