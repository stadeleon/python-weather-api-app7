import streamlit as st
from glob import glob
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
from pathlib import Path


def analyze_text(analyzed_text):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(analyzed_text)


st.title('Diary Tone')
files_list = sorted(glob('diary/*'))

pos = []
neg = []
dates = []

for file in files_list:
    with open(file, 'r') as record:
        text = record.read()

    record_scores = analyze_text(text)
    pos.append(record_scores['pos'])
    neg.append(record_scores['neg'])
    dates.append(Path(file).stem)

# dates = [Path(name).stem for name in files_list]
st.header('Positivity')
figure = px.line(x=dates, y=pos, labels={'x': 'Dates', 'y': 'Positivity'})
st.plotly_chart(figure)

st.header('Negativity')
figure = px.line(x=dates, y=neg, labels={'x': 'Dates', 'y': 'Negativity'})
st.plotly_chart(figure)


