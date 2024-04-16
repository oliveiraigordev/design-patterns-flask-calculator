from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4
from src.errors.http_unprocessable_entity import (
    HttpUnprocessableEntityError)


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler:
    def average(self, numbers: List[float]) -> float:
        return 3


def test_calculate():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    driver = MockDriverHandler()
    calculator_4 = Calculator4(driver)
    response = calculator_4.calculate(mock_request)
    assert response == {
            "data": {
                "Calculator": 4,
                "Result": 3,
            }
        }


def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 1})
    driver = MockDriverHandler()
    calculator_4 = Calculator4(driver)

    with raises(HttpUnprocessableEntityError) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == 'body mal formatado'
