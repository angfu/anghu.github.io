#streamlit run C:\Users\shimi\.spyder-py3\positioning.py
import streamlit as st

st.title('位置決め')
st.header('座標を入力')
x = st.number_input('x座標', format = '%.5f')
y = st.number_input('y座標', format = '%.5f')

st.sidebar.header('基準座標（前）')
ax1 = st.sidebar.number_input('x座標（Symbol1：前）', format = '%.5f')
ay1 = st.sidebar.number_input('y座標（Symbol 1：前）', format = '%.5f')
ax2 = st.sidebar.number_input('x座標（Symbol 2：前）', format = '%.5f')
ay2 = st.sidebar.number_input('y座標（Symbol 2：前）', format = '%.5f')
st.sidebar.header('基準座標（後）')
px1 = st.sidebar.number_input('x座標（Symbol 1：後）', format = '%.5f')
py1 = st.sidebar.number_input('y座標（Symbol 1：後）', format = '%.5f')
px2 = st.sidebar.number_input('x座標（Symbol 2：後）', format = '%.5f')
py2 = st.sidebar.number_input('y座標（Symbol 2：後）', format = '%.5f')

dx1 = px1 - ax1
dx2 = px2 - ax2
dx = (dx1 + dx2)/2

dy1 = py1 - ay1
dy2 = py2 - ay2
dy = (dy1 + dy2)/2

st.header('x座標')
st.write(x+dx)

st.header('y座標')
st.write(y+dy)