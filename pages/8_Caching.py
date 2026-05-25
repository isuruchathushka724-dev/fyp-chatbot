import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title='Caching & Performance', page_icon='⚡', layout='wide')

st.title('⚡ Session 8: Caching & Performance')
st.divider()

st.header('1. @st.cache_data — Without Cache vs With Cache')

@st.cache_data
def load_data_cached():
    time.sleep(2)
    return pd.DataFrame({
        'Feature': ['age', 'income', 'score', 'region'],
        'Importance': [0.35, 0.28, 0.19, 0.11]
    })

def load_data_no_cache():
    time.sleep(2)
    return pd.DataFrame({
        'Feature': ['age', 'income', 'score', 'region'],
        'Importance': [0.35, 0.28, 0.19, 0.11]
    })

col1, col2 = st.columns(2)
with col1:
    st.subheader('Without Cache')
    if st.button('Load (No Cache)'):
        start = time.time()
        df = load_data_no_cache()
        elapsed = time.time() - start
        st.dataframe(df)
        st.error(f'Time: {elapsed:.2f}s (slow!)')

with col2:
    st.subheader('With @st.cache_data')
    if st.button('Load (Cached)'):
        start = time.time()
        df = load_data_cached()
        elapsed = time.time() - start
        st.dataframe(df)
        st.success(f'Time: {elapsed:.2f}s (fast after first load!)')

st.divider()
st.header('2. @st.cache_data with TTL')
st.code('''
@st.cache_data(ttl=3600)  # Cache expires after 1 hour
def fetch_live_data(api_url: str) -> dict:
    import requests
    return requests.get(api_url).json()
''', language='python')

st.divider()
st.header('3. @st.cache_resource — For ML Models')
st.code('''
@st.cache_resource  # Shared across ALL users
def load_model(path: str):
    with open(path, 'rb') as f:
        return pickle.load(f)

model = load_model('models/classifier.pkl')
''', language='python')

st.divider()
st.header('4. Cache Invalidation')
st.code('''
if st.button('Reload Data'):
    load_data_cached.clear()
    st.rerun()

if st.button('Clear All Caches'):
    st.cache_data.clear()
    st.cache_resource.clear()
''', language='python')

if st.button('Clear Cache Demo'):
    load_data_cached.clear()
    st.success('Cache cleared!')
