import streamlit as st
import pandas as pd
import plotly.express as px
import io

# Set Streamlit page configuration
st.set_page_config(page_title="Student Scores Dashboard", layout="wide")

# Title of the web app
st.title("Student Scores Visualization Dashboard")

# Sample data (in lieu of a CSV file, using the provided data)
data = """
name,grade,number,kor,eng,math,info
lee,2,1,90,91,81,100
park,2,2,88,89,77,100
kim,2,3,99,99,99,100
"""
# Read the data into a DataFrame
df = pd.read_csv(io.StringIO(data))

# Display the raw data
st.subheader("Raw Data")
st.dataframe(df)

# Bar Chart: Scores by Student
st.subheader("Bar Chart: Scores by Student")
fig_bar = px.bar(
    df,
    x="name",
    y=["kor", "eng", "math", "info"],
    barmode="group",
    title="Scores by Subject for Each Student",
    labels={"name": "Student Name", "value": "Score", "variable": "Subject"}
)
st.plotly_chart(fig_bar, use_container_width=True)

# Line Chart: Scores by Student
st.subheader("Line Chart: Scores by Student")
fig_line = px.line(
    df,
    x="name",
    y=["kor", "eng", "math", "info"],
    title="Score Trends by Subject for Each Student",
    labels={"name": "Student Name", "value": "Score", "variable": "Subject"},
    markers=True
)
st.plotly_chart(fig_line, use_container_width=True)

# Average Scores by Subject
st.subheader("Average Scores by Subject")
avg_scores = df[["kor", "eng", "math", "info"]].mean().reset_index()
avg_scores.columns = ["Subject", "Average Score"]
fig_avg = px.bar(
    avg_scores,
    x="Subject",
    y="Average Score",
    title="Average Scores Across All Students",
    color="Subject"
)
st.plotly_chart(fig_avg, use_container_width=True)

# Instructions
st.markdown("""
### Instructions
- The **Bar Chart** shows individual student scores for each subject.
- The **Line Chart** displays the trend of scores across students for each subject.
- The **Average Scores** chart shows the average score for each subject across all students.
""")