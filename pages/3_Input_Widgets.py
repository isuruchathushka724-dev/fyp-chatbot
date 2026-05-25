import streamlit as st
from datetime import date, time

st.set_page_config(page_title='Input Widgets', page_icon='🎛️', layout='wide')

st.title('🎛️ Session 3: Input Widgets')
st.divider()

st.header('1. Text & Number Inputs')
name = st.text_input('Enter your name', value='Student', max_chars=50)
st.write(f'Hello, {name}!')

notes = st.text_area('Research Notes', height=100, placeholder='Describe your methodology...')

threshold = st.number_input('Classification Threshold', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
st.write(f'Threshold: {threshold}')

st.divider()
st.header('2. Selection Widgets')
model_type = st.selectbox('Select Model', ['Logistic Regression', 'Random Forest', 'SVM', 'Neural Network'])
st.write(f'Selected: {model_type}')

features = st.multiselect('Select Features', ['age', 'income', 'education', 'score'], default=['age', 'income'])
st.write(f'Features: {features}')

split = st.radio('Train/Test Split', ['Hold-out (80/20)', 'K-Fold CV', 'Stratified K-Fold'], horizontal=True)

normalise = st.checkbox('Normalise features', value=True)

st.divider()
st.header('3. Sliders')
n_trees = st.slider('Number of Trees', min_value=10, max_value=500, value=100, step=10)
age_range = st.slider('Age Range Filter', min_value=18, max_value=80, value=(25, 55))
st.write(f'Trees: {n_trees} | Age: {age_range[0]} to {age_range[1]}')

st.divider()
st.header('4. Buttons')
if st.button('Train Model', type='primary'):
    st.success('Model training started!')

st.divider()
st.header('5. File Upload')
uploaded = st.file_uploader('Upload Dataset (CSV)', type=['csv'])
if uploaded:
    import pandas as pd
    df = pd.read_csv(uploaded)
    st.success(f'Loaded {len(df)} rows!')
    st.dataframe(df.head())
