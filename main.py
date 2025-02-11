# main.py
import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker

# class for fake names
faker = Faker()

# Constants
STATUSES = ["Pass", "Acceptable", "Rejected"]
EXCEL_FILE = "test_data.xlsx"

def generate_data():
    """This function generates 10 randomized test data entries and saves them to an Excel file."""
    data = {
        "Name": [faker.name() for _ in range(10)],
        "Status": [random.choice(STATUSES) for _ in range(10)],
        "OverallEfficiency": [random.randint(1, 10) for _ in range(10)],
        "StandardOverallEfficiency": [random.randint(1, 10) for _ in range(10)],
    }
    df = pd.DataFrame(data)
    df.to_excel(EXCEL_FILE, index=False)
    return df

def plot_pie_chart(df):
    """This function displays a pie chart for the distribution of Status values."""
    status_counts = df["Status"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(status_counts, labels=status_counts.index, autopct="%1.1f%%", colors=["green", "yellow", "red"])
    ax.set_title("Status Distribution")
    st.pyplot(fig)

def plot_line_graph(df):
    """This function displays a line graph comparing Overall Efficiency and Standard Overall Efficiency."""
    fig, ax = plt.subplots()
    sns.lineplot(x=df.index, y=df["OverallEfficiency"], label="Overall Efficiency", marker="o")
    sns.lineplot(x=df.index, y=df["StandardOverallEfficiency"], label="Standard Efficiency", marker="o")
    ax.set_title("Overall Efficiency vs. Standard Efficiency")
    ax.set_xlabel("Entry Index")
    ax.set_ylabel("Efficiency Score")
    st.pyplot(fig)

# Streamlit UI
st.title("Randomized Test Data Generator & Visualizer")

if st.button("Generate Data"):
    df = generate_data()
    st.success("Randomized test data generated and saved to Excel.")
    st.dataframe(df)

    st.subheader("Data Visualizations")
    plot_pie_chart(df)
    plot_line_graph(df)
