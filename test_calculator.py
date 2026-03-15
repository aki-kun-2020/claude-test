"""計算機モジュールのテスト"""

import pytest
from calculator import add, subtract, multiply, divide, power


## add のテスト ##

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -2) == -3

def test_add_zero():
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_add_float():
    assert add(0.1, 0.2) == pytest.approx(0.3)


## subtract のテスト ##

def test_subtract_positive():
    assert subtract(5, 3) == 2

def test_subtract_negative_result():
    assert subtract(0, 5) == -5

def test_subtract_same_values():
    assert subtract(7, 7) == 0

def test_subtract_float():
    assert subtract(1.5, 0.5) == pytest.approx(1.0)


## multiply のテスト ##

def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_negative():
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6

def test_multiply_by_zero():
    assert multiply(100, 0) == 0

def test_multiply_float():
    assert multiply(2.5, 4) == pytest.approx(10.0)


## divide のテスト ##

def test_divide_exact():
    assert divide(10, 2) == 5.0

def test_divide_remainder():
    assert divide(7, 2) == 3.5

def test_divide_negative():
    assert divide(-10, 2) == -5.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="0で割ることはできません"):
        divide(1, 0)

def test_divide_zero_numerator():
    assert divide(0, 5) == 0.0


## power のテスト ##

def test_power_positive():
    assert power(2, 3) == 8

def test_power_zero_exponent():
    assert power(5, 0) == 1

def test_power_negative_exponent():
    assert power(2, -1) == pytest.approx(0.5)

def test_power_fractional_exponent():
    assert power(4, 0.5) == pytest.approx(2.0)
