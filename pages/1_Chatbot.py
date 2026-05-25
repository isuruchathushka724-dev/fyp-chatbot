import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI Chatbot', page_icon='🤖', layout='centered')

with st.sidebar:
    st.title('⚙️ Settings')
    st.divider()
    model_choice = st.selectbox('Model', ['llama-3.3-70b-versatile', 'llama3-8b-8192'], index=0)
    max_tokens = st.slider('Max tokens', 100, 2000, 1024, 100)
    system_prompt = st.text_area('System prompt', value='You are a helpful AI assistant.', height=100)
    st.divider()
    if st.button('Clear chat', use_container_width=True):
        st.session_state.messages = []
        st.rerun()

if 'messages' not in st.session_state:
    st.session_state.messages = []

st.title('🤖 AI Chatbot')
st.caption('Powered by Groq + Llama 3')
st.divider()

for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

if prompt := st.chat_input('Message AI...'):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)
    with st.chat_message('assistant'):
        with st.spinner('Thinking...'):
            try:
                client = Groq(api_key=st.secrets['GROQ_API_KEY'])
                response = client.chat.completions.create(
                    model=model_choice,
                    max_tokens=max_tokens,
                    messages=[{'role': 'system', 'content': system_prompt}] + st.session_state.messages,
                )
                reply = response.choices[0].message.content
                st.markdown(reply)
                st.session_state.messages.append({'role': 'assistant', 'content': reply})
            except Exception as e:
                st.error(f'API error: {e}')
