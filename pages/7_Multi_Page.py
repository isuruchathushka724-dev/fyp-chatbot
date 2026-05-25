import streamlit as st

st.set_page_config(page_title='Multi-Page Apps', page_icon='📱', layout='wide')

st.title('📱 Session 7: Multi-Page Apps')
st.divider()

st.header('1. File-Based Routing')
st.code('''
my_app/
├── app.py                  # Home page
└── pages/
    ├── 1_Chatbot.py        # Sidebar: "1 Chatbot"
    ├── 2_Text_Display.py   # Sidebar: "2 Text Display"
    ├── 3_Input_Widgets.py  # Sidebar: "3 Input Widgets"
    └── ...
''', language='text')

st.info('Naming convention: Leading number sets order. Underscores become spaces in sidebar.')

st.divider()
st.header('2. This App is a Multi-Page App!')
st.success('You are currently using this app as a Multi-Page App example!')

pages = {
    'app.py': 'Home — Overview of all sessions',
    '1_Chatbot.py': 'Session 9 — AI/ML Integration',
    '2_Text_Display.py': 'Session 2 — Text & Display',
    '3_Input_Widgets.py': 'Session 3 — Input Widgets',
    '4_Layouts.py': 'Session 4 — Layouts',
    '5_Data_Viz.py': 'Session 5 — Data Visualisation',
    '6_Session_State.py': 'Session 6 — Session State',
    '7_Multi_Page.py': 'Session 7 — Multi-Page Apps',
    '8_Caching.py': 'Session 8 — Caching',
    '9_Deployment.py': 'Session 10 — Deployment',
}

for file, desc in pages.items():
    st.markdown(f'- **{file}** — {desc}')

st.divider()
st.header('3. Sharing State Across Pages')
st.code('''
# Page 1 — Train model and save to session
if st.button("Train"):
    st.session_state.model = train_model()

# Page 2 — Use trained model
if st.session_state.get("model") is None:
    st.warning("Please train the model first!")
    st.stop()
''', language='python')

st.divider()
st.header('4. Programmatic Navigation')
st.code('''
if st.button("Go to Chatbot"):
    st.switch_page("pages/1_Chatbot.py")
''', language='python')

if st.button('Go to Chatbot! 🤖'):
    st.switch_page('pages/1_Chatbot.py')
