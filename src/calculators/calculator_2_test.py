from typing import Dict, List
from pytest import raises
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import (
    DriverHandlerInterface
)


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3

    def variance(self, numbers: List[float]) -> float:
        return 1568.16


def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    response = calculator_2.calculate(mock_request)

    assert isinstance(response, dict)
    assert 'data' in response
    assert 'Calculator' in response['data']
    assert 'result' in response['data']

    # Assertividade da Resposta
    assert response["data"]["result"] == 0.33
    assert response["data"]["Calculator"] == 2


# integracação entre NumpyHandler e Calculator2
def test_calculate_integration():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    response = calculator_2.calculate(mock_request)

    assert isinstance(response, dict)
    assert 'data' in response
    assert 'Calculator' in response['data']
    assert 'result' in response['data']

    # Assertividade da Resposta
    assert response["data"]["result"] == 0.79
    assert response["data"]["Calculator"] == 2


def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 1})

    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)

    with raises(Exception) as excinfo:
        calculator_2.calculate(mock_request)

    assert str(excinfo.value) == 'body mal formatado'
