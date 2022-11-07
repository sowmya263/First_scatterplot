import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.title("Scatterplot of Movie dataset")
#load the data
movie_data = pd.read_csv('movie_data.csv')

st.write(movie_data)

st.sidebar.header("Pick two variables for your scatterplot")
x_val = st.sidebar.selectbox("Pick your x-axis",movie_data.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your y-axis",movie_data.select_dtypes(include=np.number).columns.tolist())

#scatterplot
scatter = alt.Chart(movie_data, title = f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val, title = f"{x_val}"),
    alt.Y(y_val, title = f"{y_val}"),
    tooltip = [x_val,y_val])
st.altair_chart(scatter, use_container_width=True)

#calculate correlation
corr = round(movie_data[x_val].corr(movie_data[y_val]),2)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")
