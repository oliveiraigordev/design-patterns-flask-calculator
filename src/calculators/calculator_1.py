from typing import Dict
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import (
    HttpUnprocessableEntityError
)


class Calculator1:
    '''
    * Um número é divivido em 3 partes iguais.

    * A primeira parte é dividida por 4 e seu resultado somado a 7.
    Após isso o resultado é elevado ao quadrado e multiplicado por
    um valor de 0.257

    * A segunda parte é elevada à potência de 2.121, dividida por 5
    e somado a 1

    * A terceira parte se mantem o mesmo valor

    Por fim , é somado esses 3 valores e entregue o resultado
    '''
    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        splitted_number = input_data / 3
        first_process_result = self.__first_process(splitted_number)
        second_process_result = self.__second_process(splitted_number)
        calc_result = first_process_result + \
            second_process_result + \
            splitted_number
        response = self.__format_response(calc_result)

        return response

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntityError("body mal formatado")

        input_data = body["number"]
        return input_data

    def __first_process(self, fist_number: float) -> float:
        fist_part = (fist_number / 4) + 7
        second_part = (fist_part ** 2) * 0.257
        return second_part

    def __second_process(self, second_number: float) -> float:
        first_part = second_number ** 2.121
        second_part = (first_part / 5) + 1
        return second_part

    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 1,
                "result": round(calc_result, 2)
            }
        }
