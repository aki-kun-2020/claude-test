"""計算機モジュールのテスト"""

import pytest
from calculator import add, subtract, multiply, divide, power


## add のテスト ##

def test_add_positive():
    """正の数同士の足し算が正しく計算されること"""
    assert add(2, 3) == 5

def test_add_negative():
    """負の数同士の足し算が正しく計算されること"""
    assert add(-1, -2) == -3

def test_add_zero():
    """ゼロを含む足し算が正しく計算されること"""
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_add_float():
    """浮動小数点数の足し算が正しく計算されること"""
    assert add(0.1, 0.2) == pytest.approx(0.3)


## subtract のテスト ##

def test_subtract_positive():
    """正の数同士の引き算が正しく計算されること"""
    assert subtract(5, 3) == 2

def test_subtract_negative_result():
    """結果が負になる引き算が正しく計算されること"""
    assert subtract(0, 5) == -5

def test_subtract_same_values():
    """同じ値の引き算がゼロになること"""
    assert subtract(7, 7) == 0

def test_subtract_float():
    """浮動小数点数の引き算が正しく計算されること"""
    assert subtract(1.5, 0.5) == pytest.approx(1.0)


## multiply のテスト ##

def test_multiply_positive():
    """正の数同士の掛け算が正しく計算されること"""
    assert multiply(3, 4) == 12

def test_multiply_negative():
    """負の数を含む掛け算の符号が正しいこと"""
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6

def test_multiply_by_zero():
    """ゼロとの掛け算がゼロになること"""
    assert multiply(100, 0) == 0

def test_multiply_float():
    """浮動小数点数の掛け算が正しく計算されること"""
    assert multiply(2.5, 4) == pytest.approx(10.0)


## divide のテスト ##

def test_divide_exact():
    """割り切れる割り算が正しく計算されること"""
    assert divide(10, 2) == 5.0

def test_divide_remainder():
    """割り切れない割り算が正しく計算されること"""
    assert divide(7, 2) == 3.5

def test_divide_negative():
    """負の数の割り算が正しく計算されること"""
    assert divide(-10, 2) == -5.0

def test_divide_by_zero():
    """ゼロで割った場合にValueErrorが発生すること"""
    with pytest.raises(ValueError, match="0で割ることはできません"):
        divide(1, 0)

def test_divide_zero_numerator():
    """ゼロを割った場合にゼロが返ること"""
    assert divide(0, 5) == 0.0


## power のテスト ##

def test_power_positive():
    """正の指数のべき乗が正しく計算されること"""
    assert power(2, 3) == 8

def test_power_zero_exponent():
    """指数がゼロの場合に1が返ること"""
    assert power(5, 0) == 1

def test_power_negative_exponent():
    """負の指数のべき乗が正しく計算されること"""
    assert power(2, -1) == pytest.approx(0.5)

def test_power_fractional_exponent():
    """小数の指数（平方根など）が正しく計算されること"""
    assert power(4, 0.5) == pytest.approx(2.0)
