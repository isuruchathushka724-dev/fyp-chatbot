import streamlit as st

st.set_page_config(page_title='Session State & Forms', page_icon='🔄', layout='wide')

st.title('🔄 Session 6: Session State & Forms')
st.divider()

st.header('1. Session State - Counter')
if 'count' not in st.session_state:
    st.session_state.count = 0

col1, col2, col3 = st.columns(3)
if col1.button('➕ Increment'):
    st.session_state.count += 1
if col2.button('➖ Decrement'):
    st.session_state.count -= 1
if col3.button('🔄 Reset'):
    st.session_state.count = 0

st.metric('Count', st.session_state.count)

st.divider()
st.header('2. Session State - ML Workflow')
if 'is_trained' not in st.session_state:
    st.session_state.is_trained = False
    st.session_state.accuracy = 0.0

if st.button('Train Model', type='primary'):
    with st.spinner('Training...'):
        import time
        time.sleep(1)
        st.session_state.is_trained = True
        st.session_state.accuracy = 0.945
        st.success('Model trained!')

if st.session_state.is_trained:
    st.metric('Model Accuracy', f'{st.session_state.accuracy:.1%}')
else:
    st.warning('Please train the model first.')

st.divider()
st.header('3. Forms')
with st.form('patient_form'):
    st.subheader('Patient Information')
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input('Age', 0, 120, 35)
        gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
    with col2:
        weight = st.number_input('Weight (kg)', 30.0, 200.0, 70.0)
        height = st.number_input('Height (cm)', 100.0, 250.0, 170.0)
    symptoms = st.multiselect('Symptoms', ['Fever', 'Cough', 'Fatigue', 'Breathlessness'])
    submitted = st.form_submit_button('Run Diagnosis', type='primary')

if submitted:
    bmi = weight / ((height/100) ** 2)
    st.metric('BMI', f'{bmi:.1f}')
    st.info(f'Processing {age}yr {gender} patient with {len(symptoms)} symptoms...')
