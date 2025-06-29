# app.py
import streamlit as st

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

st.title("Grade Calculator")
marks = st.text_input("Enter your marks (0-100):")

if st.button("Calculate Grade"):
    try:
        marks = float(marks)
    except ValueError:
        result = "Invalid marks!"
    else:
        result = calculate_grade(marks)

    st.success(f"Result: {result}")
