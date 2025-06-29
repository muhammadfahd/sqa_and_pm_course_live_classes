# test_grade.py
from grade import calculate_grade

def test_invalid_input_string():
    assert calculate_grade("abc") == "Invalid marks!"

def test_invalid_input_negative():
    assert calculate_grade(-10) == "Invalid marks!"

def test_invalid_input_above_100():
    assert calculate_grade(150) == "Invalid marks!"

def test_grade_A():
    assert calculate_grade(95) == "A"

def test_grade_B():
    assert calculate_grade(85) == "B"

def test_grade_C():
    assert calculate_grade(75) == "C"

def test_grade_D():
    assert calculate_grade(65) == "D"

def test_grade_F():
    assert calculate_grade(50) == "F"
