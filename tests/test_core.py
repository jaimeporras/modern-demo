import pytest
from modern_demo.core import process_numbers


# 🔹 Basic test (explicit assertions)
def test_process_numbers():
    assert process_numbers([1, -1, 3, 0]) == [2, 6]
    assert process_numbers([]) == []


# 🔹 Parametrized test (runs multiple cases automatically)
@pytest.mark.parametrize(
    "input_data,expected",
    [
        ([1, 2, -1], [2, 4]),   # doubles positives, ignores negative
        ([0, -5, 7], [14]),     # ignores zero and negatives
        ([], []),               # empty input stays empty
    ]
)
def test_process_numbers_param(input_data, expected):
    assert process_numbers(input_data) == expected
