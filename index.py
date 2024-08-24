import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("Data Dashboard")
uploaded_file=st.file_uploader("Choose a CSV file", type='csv')

if uploaded_file is not None:
    st.write("File Uploaded...")
    df=pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    cols=df.columns.to_list()
    selected_cols= st.selectbox("Select column to filter by", cols)
    unique_vals=df[selected_cols].unique()
    selected_vals=st.selectbox("Select value", unique_vals)

    filtered_df=df[df[selected_cols]== selected_vals]
    st.write(filtered_df)
    st.subheader("Plot Data")
    x_col = st.selectbox("Select x-axis column", cols)
    y_col = st.selectbox("Select y-axis column", cols)

    chart_type = st.selectbox("Select type of graph", options=["Line", "Scatter", "Bar Chart", "Box Plot"])

    if st.button("Generate Plot"):
        if chart_type == "Line":
            st.line_chart(filtered_df.set_index(x_col)[y_col])
        elif chart_type == "Scatter":
            st.write(st.plotly_chart(filtered_df.plot.scatter(x=x_col, y=y_col)))
        elif chart_type == "Bar Chart":
            st.bar_chart(filtered_df.set_index(x_col)[y_col])
        elif chart_type == "Box Plot":
            st.write(st.plotly_chart(filtered_df[[x_col, y_col]].boxplot(by=x_col)))
else:
    st.write("Waiting on File Upload...")