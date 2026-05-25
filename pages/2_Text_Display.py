import streamlit as st

st.set_page_config(page_title='Text & Display', page_icon='📝', layout='wide')

st.title('📝 Session 2: Text & Display Elements')
st.divider()

st.header('1. Text Display Functions')
st.title('st.title() — Main Title')
st.header('st.header() — Section Header')
st.subheader('st.subheader() — Sub-section')
st.text('st.text() — Plain monospaced text')
st.write('st.write() — Smart write, auto-detects type')

st.divider()
st.header('2. Markdown')
st.markdown('''
**Bold text**, *italic text*, inline code
- List item 1
- List item 2
''')

st.divider()
st.header('3. Code Display')
st.code('''
def greet(name):
    return f"Hello, {name}!"
''', language='python')

st.divider()
st.header('4. Notification Messages')
st.success('Success message!')
st.info('Info message!')
st.warning('Warning message!')
st.error('Error message!')

st.divider()
st.header('5. Metric Cards')
col1, col2, col3, col4 = st.columns(4)
col1.metric('Accuracy', '94.5%', '+2.1%')
col2.metric('Precision', '91.2%', '-0.8%')
col3.metric('Recall', '96.3%', '+1.5%')
col4.metric('F1 Score', '93.7%', '+0.6%')

st.divider()
st.header('6. LaTeX')
st.latex(r'\hat{y} = \sigma(W \cdot X + b)')

st.divider()
st.header('7. JSON Display')
st.json({'model': 'Random Forest', 'accuracy': 0.945, 'features': ['age', 'income']})
