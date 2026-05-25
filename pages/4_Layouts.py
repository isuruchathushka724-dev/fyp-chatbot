import streamlit as st

st.set_page_config(page_title='Layouts', page_icon='🗂️', layout='wide')

st.title('🗂️ Session 4: Layouts & Containers')
st.divider()

st.header('1. Columns')
col1, col2, col3 = st.columns(3)
col1.metric('Accuracy', '94.5%', '+2%')
col2.metric('Loss', '0.082', '-0.01')
col3.metric('F1', '93.7%', '+1%')

st.divider()
left, right = st.columns([2, 1])
with left:
    st.subheader('Left Column (wider)')
    st.write('This column is twice as wide as the right one.')
with right:
    st.subheader('Right Column')
    st.write('Narrower column.')

st.divider()
st.header('2. Tabs')
tab1, tab2, tab3 = st.tabs(['Data Overview', 'Model Training', 'Predictions'])
with tab1:
    st.write('Dataset overview content here.')
with tab2:
    st.write('Model training controls here.')
with tab3:
    st.write('Prediction results here.')

st.divider()
st.header('3. Expander')
with st.expander('Advanced Configuration', expanded=False):
    st.write('These are advanced settings.')
    lr = st.number_input('Learning Rate', 0.0001, 0.1, 0.001)
    bs = st.selectbox('Batch Size', [16, 32, 64, 128])

st.divider()
st.header('4. Container with Border')
with st.container(border=True):
    st.subheader('Model Summary')
    st.write('Algorithm: Random Forest | Trees: 200 | Depth: 15')

st.divider()
st.header('5. Progress & Spinner')
import time
if st.button('Simulate Training'):
    progress = st.progress(0, text='Initialising...')
    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1, text=f'Training epoch {i+1}/100...')
    progress.empty()
    st.success('Training complete!')
