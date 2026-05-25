import streamlit as st

st.set_page_config(
    page_title='Streamlit Demo App',
    page_icon='🚀',
    layout='wide',
    initial_sidebar_state='expanded'
)

st.title('🚀 Streamlit Development — IT41043')
st.subheader('From Basics to Deployment | Horizon Campus 2026')
st.divider()

col1, col2, col3, col4 = st.columns(4)
col1.metric('Sessions', '10')
col2.metric('Pages', '8')
col3.metric('AI Model', 'Llama 3')
col4.metric('Deployed', 'Streamlit Cloud')

st.divider()
st.markdown('''
### 📚 Sessions
| Session | Topic | Page |
|---------|-------|------|
| 1 | Introduction & Setup | Home |
| 2 | Text & Display Elements | 📝 Text Display |
| 3 | Input Widgets | 🎛️ Input Widgets |
| 4 | Layouts & Containers | 🗂️ Layouts |
| 5 | Data & Visualisation | 📊 Data Viz |
| 6 | Session State & Forms | 🔄 Session State |
| 7 | Multi-Page Apps | ✅ This App! |
| 8 | Caching & Performance | ⚡ Caching |
| 9 | AI/ML Integration | 🤖 Chatbot |
| 10 | Deployment | 🚀 Deployment |
''')

st.divider()
st.info('👈 Sidebar එකෙන් navigate කරන්න!')
