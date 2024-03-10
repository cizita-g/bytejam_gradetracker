import streamlit as st

def main():
    st.title('Grade Tracker')

    # Input box for entering total marks
    total_marks = st.number_input('Enter Total Marks', min_value=0, max_value=500, step=1, value=0)

    # Calculate and display GPA and Grade
    if total_marks > 0:
        gpa = total_marks / 125.0
        grade = calculate_grade(gpa)

        # Display GPA and Grade
        st.subheader(f'GPA: {gpa:.2f}')
        st.subheader(f'Grade: {grade}')

def calculate_grade(gpa):
    if gpa >= 3.6:
        return 'A+'
    elif 3.2 <= gpa < 3.6:
        return 'A'
    elif 2.8 <= gpa < 3.2:
        return 'B+'
    elif 2.4 <= gpa < 2.8:
        return 'B'
    elif 2.0 <= gpa < 2.4:
        return 'C+'
    else:
        return 'D'

main()
