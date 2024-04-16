from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator3


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


# remoção da herança para não precisar criar todas as funções
# class MockDriverHandler(DriverHandlerInterface):
class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 3


class MockDriverHandler:
    def variance(self, numbers: List[float]) -> float:
        return 1568.16


def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    driver = MockDriverHandlerError()
    calculator_3 = Calculator3(driver)

    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == \
        'Falha no processo: Variância menor que multiplicação'


def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    driver = MockDriverHandler()
    calculator_3 = Calculator3(driver)
    response = calculator_3.calculate(mock_request)

    assert response == {
            "data": {
                "Calculator": 3,
                "Value": 1568.16,
                "Success": True
            }
        }
