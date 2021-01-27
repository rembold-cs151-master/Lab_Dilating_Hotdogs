"""
Testing script for Lab 03

You don't need to do anything with this script,
but you are welcome to look it over!
"""

import pytest
import Lab03

def is_within_percent(submitted_value, real_value, percent):
    plus_minus = real_value * percent/100
    return (real_value - plus_minus) < submitted_value < (real_value + plus_minus)


def test_no_movement():
    value = Lab03.moving_time(0)
    assert is_within_percent(value, 21.6, 0.01)

def test_10_percent():
    value = Lab03.moving_time(0.1 * 3E8)
    assert is_within_percent(value, 21.7088, 0.01)

def test_50_percent():
    value = Lab03.moving_time(0.5 * 3E8)
    assert is_within_percent(value, 24.94153, 0.01)

def test_95_percent():
    value = Lab03.moving_time(0.95 * 3E8)
    assert is_within_percent(value, 69.17536, 0.01)

def test_99_percent():
    value = Lab03.moving_time(0.99 * 3E8)
    assert is_within_percent(value, 153.1183, 0.01)

def test_ANS_defined():
    assert "ANS" in dir(Lab03), "It looks like you didn't define ANS for the needed speed to double the measured time!"

def test_double_time_speed_correct():
    value = Lab03.moving_time(Lab03.ANS)
    assert is_within_percent(value, 43.2, 0.05)
