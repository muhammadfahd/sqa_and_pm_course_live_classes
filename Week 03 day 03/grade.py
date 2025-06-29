# grade.py

def calculate_grade(marks):
    if not isinstance(marks, (int, float)) or marks < 0 or marks > 100:
        return "Invalid marks!"
    elif marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
