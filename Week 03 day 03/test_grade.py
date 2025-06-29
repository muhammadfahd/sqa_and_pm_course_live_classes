# test_grade.py

import pytest
from grade import calculate_grade

def test_grade_a():
    assert calculate_grade(95) == "A"

def test_grade_b():
    assert calculate_grade(85) == "B"

def test_grade_c():
    assert calculate_grade(75) == "C"

def test_grade_d():
    assert calculate_grade(65) == "D"

def test_grade_f():
    assert calculate_grade(45) == "F"

def test_invalid_below_range():
    assert calculate_grade(-5) == "Invalid marks!"

def test_invalid_above_range():
    assert calculate_grade(120) == "Invalid marks!"

def test_invalid_non_numeric():
    assert calculate_grade("abc") == "Invalid marks!"
