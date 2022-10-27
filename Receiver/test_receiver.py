import os, sys
from unittest import TestCase, mock

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Receiver.receiver import convert_to_json, input_collector
from compute_statistics import (
    convert_to_single_dimension_dict,
    calculate_statistics
)
from receiver import print_stats


def test_convert_to_json():
    data = """
    [
        {"Temperature": 42, "StateOfCharge": 42}, 
        {"Temperature": 35, "StateOfCharge": 45}
    ]
    """
    assert None == convert_to_json(data)[0]


def test_negative_convert_to_json():
    data = """
    [
        {"Temperature": 42, "StateOfCharge": 42}, 
        {"Temperature": 35, "StateOfCharge": 45}
    """
    err = convert_to_json(data)[0]
    assert type(err) == ValueError
    assert  str(err) == "Invalid JSON format"


def test_calculate_statistics():
    given_data = [
            {"Temperature": 42, "StateOfCharge": 19},
            {"Temperature": 50, "StateOfCharge": 30},
            {"Temperature": 80, "StateOfCharge": 22},
            {"Temperature": 60, "StateOfCharge": 27},
            {"Temperature": 65, "StateOfCharge": 34},
        ]
    expected_result = [
        "the minimum value of 'Temperature' is 42",
        "the maximum value of 'Temperature' is 80",
        "simple moving average of last 5 values for 'Temperature' is 59.4",
        "the minimum value of 'StateOfCharge' is 19",
        "the maximum value of 'StateOfCharge' is 34",
        "simple moving average of last 5 values for 'StateOfCharge' is 26.4",
    ]
    assert calculate_statistics(given_data) == expected_result


def test_print_stats():
    given_data = [
            {"Temperature": 28, "StateOfCharge": 19},
            {"Temperature": 50, "StateOfCharge": 30},
            {"Temperature": 80, "StateOfCharge": 22},
            {"Temperature": 60, "StateOfCharge": 47},
            {"Temperature": 65, "StateOfCharge": 34},
        ]
    expected_output = r"""
the minimum value of 'Temperature' is 28
the maximum value of 'Temperature' is 80
simple moving average of last 5 values for 'Temperature' is 56.6
the minimum value of 'StateOfCharge' is 19
the maximum value of 'StateOfCharge' is 47
simple moving average of last 5 values for 'StateOfCharge' is 30.4
""".strip()
    output = ""

    def send_output_as_file(data):
        nonlocal output
        output += data

    print_stats(given_data, send_output_as_file)
    assert output == expected_output


def test_convert_to_single_dimension_dict():
    data = [
        {"Temperature": 42, "StateOfCharge": 42},
        {"Temperature": 50, "StateOfCharge": 30},
        {"Temperature": 65, "StateOfCharge": 18},
    ]

    expected_data = {"Temperature": [42, 50, 65], "StateOfCharge": [42, 30, 18]}
    assert convert_to_single_dimension_dict(data) == expected_data


def test_input_collector():
    given_data = """{"Temperature": 42, "StateOfCharge": 42}"""
    
    with mock.patch('builtins.input', return_value=given_data):
        assert input_collector(1) == [{"Temperature": 42, "StateOfCharge": 42}]

def test_negative_input_collector():
    given_data = """{"Temperature": 42, "StateOfCharge": 42"""
    
    with mock.patch('builtins.input', return_value=given_data):
        with TestCase().assertRaises(ValueError) as error:
            input_collector(1)
        assert str(error.exception) == "Invalid JSON format"
