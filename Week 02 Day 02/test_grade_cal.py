import pytest
from grade_calculator import grade_calculator

def test_grade_a():
    assert grade_calculator(95) == "A"

def test_grade_b():
    assert grade_calculator(80) == "B"

def test_grade_c():
    assert grade_calculator(65) == "C"

def test_grade_d():
    assert grade_calculator(45) == "D"

def test_grade_f():
    assert grade_calculator(20) == "F"

# EP and BVA cases
def test_boundary_b_to_a():
    assert grade_calculator(89) == "B"
    assert grade_calculator(90) == "G"

def test_boundary_c_to_b():
    assert grade_calculator(74) == "C"
    assert grade_calculator(75) == "B"

def test_boundary_d_to_c():
    assert grade_calculator(59) == "D"
    assert grade_calculator(60) == "C"

def test_boundary_f_to_d():
    assert grade_calculator(39) == "F"
    assert grade_calculator(40) == "D"

# Invalid input
def test_invalid_below_range():
    with pytest.raises(ValueError):
        grade_calculator(-1)

def test_invalid_above_range():
    with pytest.raises(ValueError):
        grade_calculator(101)
