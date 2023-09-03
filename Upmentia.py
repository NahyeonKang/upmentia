import streamlit as st
from streamlit_chat import message
from audiorecorder import audiorecorder
import requests
import io
from PIL import Image
with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
        image = Image.open(f'assets/logo.png')
        st.image(image)
    with col2:
        st.title(' ')
        st.title(' ')
        st.title(' ')
        st.subheader('회상요법을 통한 치매 인지 재활')

st.markdown('''
#### :ear:어르신의 추억을 들려주세요!  
#### :point_left:어떤 이야기를 들려주고 싶으신가요? 왼쪽에서 주제를 선택해보세요''')
