import email.message

import streamlit as st
import plotly.express as px
from backend import get_forecast_data, prepare_images_list

st.title('Weather forecast for t next days')

place = st.text_input('Place', key='place', value='Kiev')
number_of_days = st.slider('Forecast days', min_value=1, max_value=5,
                           help="Select the number of forecasted days")
option = st.selectbox('Select data to view:', ("Temperature", "Sky"))
st.subheader(f"{option} for the next {number_of_days} days in {place}")

try:
    data = get_forecast_data(place, number_of_days)

    match option:
        case 'Temperature':
            figure = px.line(x=data['dates'], y=data['temperatures'], labels={"x": "Date", "y": "Temperature C"})
            st.plotly_chart(figure)
        case 'Sky':
            images_list = prepare_images_list(data['sky'])
            st.image(images_list, width=80)
except Exception as e:
    st.info(e)