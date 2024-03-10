import streamlit as st
import pandas as pd

def main():
    st.title('Grade Tracker')

    # Create a DataFrame to store grades
    grades_df = pd.DataFrame(columns=['Subject', 'Marks'])

    # Sidebar for adding new grades
    st.sidebar.header('Add New Grade')
    new_subject = st.sidebar.text_input('Subject')
    new_marks = st.sidebar.number_input('Marks', min_value=0, max_value=500, step=1)

    if st.sidebar.button('Add Grade'):
        grades_df = grades_df.append({'Subject': new_subject, 'Marks': new_marks}, ignore_index=True)
        st.sidebar.success('Grade added successfully!')

    # Display the grades
    st.header('Your Grades')
    st.dataframe(grades_df)

    # Calculate and display GPA and Grade
    if not grades_df.empty:
        total_marks = grades_df['Marks'].sum()
        gpa = total_marks / 25.0
        grade = calculate_grade(gpa)
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

if __name__ == '__main__':
    main()
