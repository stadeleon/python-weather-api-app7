import streamlit as st
import plotly.express as px

st.title('Weather forecast for t next days')

place = st.text_input('Place', key='place')
number_of_days = st.slider('Forecast days', min_value=1, max_value=5,
                           help="Select the number of forecasted days")
option = st.selectbox('Select data to view:', ("Temperature", "Sky"))

st.subheader(f"{option} for the next {number_of_days} days in {place}")

dates = ['2022-25-10', '2022-26-10', '2022-27-10']
temperatures = [10, 11, 13]
figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature C"})
st.plotly_chart(figure)
