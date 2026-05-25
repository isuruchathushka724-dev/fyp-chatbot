import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Data & Visualisation', page_icon='📊', layout='wide')

st.title('📊 Session 5: Data & Visualisation')
st.divider()

df = pd.DataFrame({
    'Patient_ID': range(1, 6),
    'Age': [34, 45, 56, 29, 67],
    'Diagnosis': ['Positive','Negative','Positive','Negative','Positive'],
    'Confidence': [0.92, 0.87, 0.95, 0.73, 0.89]
})

st.header('1. DataFrame')
st.dataframe(df, use_container_width=True)

st.divider()
st.header('2. Native Charts')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Model A', 'Model B', 'Baseline'])
tab1, tab2, tab3 = st.tabs(['Line', 'Bar', 'Area'])
with tab1:
    st.line_chart(chart_data)
with tab2:
    st.bar_chart(chart_data)
with tab3:
    st.area_chart(chart_data)

st.divider()
st.header('3. Plotly Interactive Charts')
models = ['Logistic Reg', 'Random Forest', 'SVM', 'XGBoost']
scores = [0.87, 0.94, 0.91, 0.96]
fig = go.Figure(go.Bar(
    x=models, y=scores,
    marker_color=['#636EFA','#EF553B','#00CC96','#AB63FA'],
    text=[f'{s:.0%}' for s in scores], textposition='outside'
))
fig.update_layout(title='Model Accuracy Comparison', yaxis_range=[0.8, 1.0])
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.header('4. Matplotlib - Confusion Matrix')
cm = np.array([[85, 5], [8, 102]])
fig2, ax = plt.subplots(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
    xticklabels=['Pred Neg','Pred Pos'],
    yticklabels=['True Neg','True Pos'], ax=ax)
ax.set_title('Confusion Matrix')
st.pyplot(fig2)
plt.close(fig2)
