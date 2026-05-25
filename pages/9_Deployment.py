import streamlit as st

st.set_page_config(page_title='Deployment', page_icon='🚀', layout='wide')

st.title('🚀 Session 10: Deployment')
st.divider()

st.header('1. Pre-Deployment Checklist')
items = [
    'requirements.txt has all packages',
    'secrets in .streamlit/secrets.toml (not in code!)',
    'headless=true in config.toml',
    'runtime.txt specifies Python version',
    'Tested locally with streamlit run app.py',
    'GitHub repo is up to date',
]
for item in items:
    st.checkbox(item)

st.divider()
st.header('2. Deployment Options')
tab1, tab2, tab3 = st.tabs(['Streamlit Cloud', 'Render', 'Docker'])

with tab1:
    st.subheader('Streamlit Community Cloud (Free)')
    st.success('Recommended for FYP!')
    st.markdown('''
1. Push code to GitHub
2. Go to share.streamlit.io
3. Click "New app"
4. Select repo, branch, main file
5. Add secrets in Advanced settings
6. Click Deploy!
    ''')
    st.code('# requirements.txt\nstreamlit==1.56.0\ngroq>=0.9.0', language='text')

with tab2:
    st.subheader('Render (Free Tier)')
    st.info('Good for larger models')
    st.code('streamlit run app.py --server.port  --server.headless true', language='bash')

with tab3:
    st.subheader('Docker')
    st.info('Best for reproducible environments')
    st.code('''FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py"]''', language='dockerfile')

st.divider()
st.header('3. Deployment Comparison')
import pandas as pd
df = pd.DataFrame({
    'Platform': ['Streamlit Cloud', 'Render', 'Hugging Face', 'Docker'],
    'Cost': ['Free', 'Free', 'Free', 'Free (local)'],
    'RAM': ['1 GB', '512 MB', '16 GB GPU', 'Unlimited'],
    'Setup Time': ['< 5 min', '10 min', '5 min', '30 min'],
    'Best For': ['Most FYP apps', 'Medium models', 'Heavy DL/LLM', 'Reproducible']
})
st.dataframe(df, use_container_width=True)

st.divider()
st.header('4. This App!')
st.success('This app is deployed on Streamlit Cloud!')
st.code('fyp-chatbot-fnvu7zsj6m8vappnvct2tg.streamlit.app', language='text')
