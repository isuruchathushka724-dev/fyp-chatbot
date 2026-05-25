import streamlit as st

st.set_page_config(
    page_title='FYP AI Chatbot',
    page_icon='🤖',
    layout='wide',
    initial_sidebar_state='expanded'
)

st.title('🤖 FYP AI Chatbot')
st.subheader('Powered by Groq + Llama 3')
st.divider()

st.markdown('''
### Navigation
Sidebar එකෙන් navigate කරන්න:
- **Chatbot** — AI chatbot එක use කරන්න
''')
