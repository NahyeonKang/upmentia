import streamlit as st
from streamlit_chat import message
from audiorecorder import audiorecorder
import requests
import io
from PIL import Image
from streamlit_card import card
from streamlit_extras.switch_page_button import switch_page
import base64
import os

st.set_page_config(page_title="Upmentia", page_icon=":thumbsup:", initial_sidebar_state="collapsed")

def speak_to(who):
    st.session_state["who"]=who

def load_image(where):
    pwd = os.getcwd()
    file = os.path.join(pwd, "assets", f"{where}.jpg")
    with open(file, "rb") as f:
        encoded = base64.b64encode(f.read())

    data = "data:image/png;base64," + encoded.decode("utf-8")
    return data


if "newsession" not in st.session_state:
    st.session_state["newsession"] = True
else:
    st.session_state["newsession"] = False

if "who" not in st.session_state:
    st.session_state["who"] = "가족"

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
#### :smiley:누구랑 이야기할까요? ''')
wife, husband, son, daughter, grands, grandd, teacher = st.columns(7)

with wife:
    st.button('아내', on_click=speak_to, args=['아내'])
with husband:
    st.button('남편', on_click=speak_to, args=['남편'])
with son:
    st.button('아들', on_click=speak_to, args=['아들'])
with daughter:
    st.button('딸', on_click=speak_to, args=['딸'])
with grands:
    st.button('손자', on_click=speak_to, args=['손자'])
with grandd:
    st.button('손녀', on_click=speak_to, args=['손녀'])
with teacher:
    st.button('요양사', on_click=speak_to, args=['치료사'])

st.markdown('''
#### 어떤 이야기를 들려주고 싶으신가요? 주제를 선택해보세요:point_down:''')
family, hometown, pot = st.columns(3)
with family:
    familypage = card(
        title="가족",
        image=load_image("family"),
        styles={
            "card": {
                "width": "300px",
                "height": "300px",
                "margin": "0px",
                "padding": "0px",
                }
            },
        )

    if familypage:
        switch_page("가족")

with hometown:
    hometownpage = card(
        title="고향",
        image=load_image("hometown"),
        styles={
            "card": {
                "width": "300px",
                "height": "300px",
                "margin": "0px",
                "padding": "0px",
                }
            },
        )

    if hometownpage:
        switch_page("고향")

with pot:
    potpage = card(
        title="양은냄비",
        image=load_image("pot"),
        styles={
            "card": {
                "width": "300px",
                "height": "300px",
                "margin": "0px",
                "padding": "0px",
                }
            },
        )

    if potpage:
        switch_page("양은냄비")

if __name__ == "__main__":
    if st.session_state["newsession"]:
        try:
            from backend import init
            
        except:
            pass
