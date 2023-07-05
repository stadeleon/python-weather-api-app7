import streamlit as st
import plotly.express as pt
import pandas as pd

st.title('In Search for Happiness')

df = pd.read_csv('happy.csv')
headers = [column.title().replace('_', ' ')
           if len(column) > 3 else column.upper() for column in df.columns]

x_line = st.selectbox("Select the data for the X-axis", headers)
y_line = st.selectbox("Select the data for the Y-axis", headers)

st.header(f"{x_line} and {y_line}")

figure = pt.scatter(
                    x=df[x_line.replace(' ', '_').lower()],
                    y=df[y_line.replace(' ', '_').lower()],
                    labels={"x": x_line, "y": y_line})
# figure = pt.scatter(df,
#                     x=x_line.replace(' ', '_').lower(),
#                     y=y_line.replace(' ', '_').lower(),
#                     labels={"x": x_line, "y": y_line}
#                     )
st.plotly_chart(figure)

