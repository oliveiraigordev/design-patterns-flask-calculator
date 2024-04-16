from flask import Blueprint, jsonify, request
from src.errors.error_controller import handle_errors
from src.main.factories.calculator_1_factory import (
    calculator_1_factory
)
from src.main.factories.calculator_2_factory import (
    calculator_2_factory
)
from src.main.factories.calculator_3_factory import (
    calculator_3_factory
)
from src.main.factories.calculator_4_factory import (
    calculator_4_factory
)


calc_route_bp = Blueprint('calc_routes', __name__)


@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
    try:
        calc = calculator_1_factory()
        response = calc.calculate(request)
        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response['body']), error_response['status_code']


@calc_route_bp.route('/calculator/2', methods=['POST'])
def calculator_2():
    try:
        calc = calculator_2_factory()
        response = calc.calculate(request)
        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response['body']), error_response['status_code']


@calc_route_bp.route('/calculator/3', methods=['POST'])
def calculator_3():
    try:
        calc = calculator_3_factory()
        response = calc.calculate(request)
        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response['body']), error_response['status_code']


@calc_route_bp.route('/calculator/4', methods=['POST'])
def calculator_4():
    try:
        calc = calculator_4_factory()
        response = calc.calculate(request)
        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response['body']), error_response['status_code']
