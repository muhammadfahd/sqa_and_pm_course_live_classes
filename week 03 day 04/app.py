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

# 🧪 App UI — Exploratory Inputs
st.title("🧪 Exploratory Grade Calculator")

# Input Fields for Exploration
student_name = st.text_input("Enter Student Name:")
subject = st.selectbox("Select Subject:", ["Math", "English", "Science", "History", "⚗ Chemistry", "🔥 Fire Safety"])
marks_input = st.text_input("Enter Marks (0-100):")
remarks = st.text_area("Additional Comments (optional):")

# Button
if st.button("Calculate Grade"):
    st.subheader("🧾 Test Output")

    try:
        marks = float(marks_input)
    except ValueError:
        result = "Invalid marks!"
    else:
        result = calculate_grade(marks)

    st.write("**Student:**", student_name)
    st.write("**Subject:**", subject)
    st.write("**Marks Entered:**", marks_input)
    st.write("**Remarks:**", remarks)
    st.success(f"🎓 Grade: {result}")
