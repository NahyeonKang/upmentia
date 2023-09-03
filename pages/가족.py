import streamlit as st
from streamlit_chat import message
from audiorecorder import audiorecorder
import requests
import io
from PIL import Image
import os 

chat_url = "http://localhost:8000/chat"
stt_url = "http://localhost:8000/stt"
dalle_url = "http://localhost:8000/dalle"

firstmsg = """당신은 치매환자의 가족입니다. 치매환자가 과거를 회상하고 행복한 추억에 잠길 수 있도록 {subject}에 대한 이야기를 나눌 것입니다. 
치매환자가 {subject}에 대한 행복한 추억을 회상할 수 있도록 {subject}에 관한 질문을 하나 해주세요.
질문은 짧고 대답하기 쉬운 질문을 해주세요."""

sysmsg = """당신은 치매환자의 가족입니다. 치매환자가 과거를 회상하고 행복한 추억에 잠길 수 있도록 {subject}에 대한 이야기를 나눌 것입니다. 
치매환자의 이야기에 따라 상냥하고 긍정적인 반응과 함께 꼬리질문을 해주세요.
꼬리질문은 짧고 대답하기 쉬운 질문을 해주세요."""
## page 변수
familymsg = 'familymessages'
familyfirst = 'familyfirst'
familysubject = "가족"
familyfirstmsg = firstmsg.format(subject = familysubject)

if familymsg not in st.session_state:
    st.session_state[familymsg] = []
if familyfirst not in st.session_state:
    st.session_state[familyfirst] = True

def chat(text):
    user_turn = {"role":"user", "content": text}
    system_msg = {"role":"system", "content":sysmsg.format(subject=familysubject)}
    messages = [i for i in st.session_state[familymsg] if i["role"] != "img"]
    resp = requests.post(chat_url, json={"messages": messages + [user_turn] + [system_msg]})
    assistant_turn = resp.json()
    st.session_state[familymsg].append(user_turn)

    if len(text)>4:
        translate_system_msg = {"role":"system", "content":"Translate to English and turn it into a noun phrase. Just show me a noun phrase"}
        resp_img = requests.post(dalle_url, json={"messages": [user_turn] + [translate_system_msg]})
        img_url = resp_img.json()['url']
        print(img_url)
        img_turn = {"role":"img", "content": img_url}
        st.session_state[familymsg].append(img_turn)
    
    st.session_state[familymsg].append(assistant_turn)
    


def stt(audio_bytes):
    audio_file = io.BytesIO(audio_bytes)
    files = {"audio_file": ("audio.wav", audio_file, "audio/wav")}
    response = requests.post(stt_url, files=files)
    text = response.json()['text']
    return text


with st.container():
    col11, col12, col13 = st.columns(3)
    with col11:
        st.empty()
    with col12:
        pwd = os.getcwd()
        img_path = os.path.join(pwd, "family.jpg")
        image = Image.open(img_path)
        st.image(image)
    with col13:
        st.empty()

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.empty() 
    with col2:
        st.markdown(f"<h1 style='text-align: center;'>{familysubject}</h1>", unsafe_allow_html=True)

    with col3:
        st.empty() 

row1 = st.container()
row2 = st.container()
row3 = st.container()

with row3:
    with st.container():
        input_text = st.chat_input("말하지 않고 직접 입력하기")
        if input_text:
            chat(input_text)

with row2:
    col21, col22 = st.columns([5, 1])
    with col21:
        st.empty()
    with col22:
        audio = audiorecorder("말하기", "듣고있어요")
        if len(audio) > 0:
            audio_bytes = audio.tobytes()
            text = stt(audio_bytes)
            if "음성인식이 실패했습니다." in text:
                st.session_state[familymsg].append({"role":"assistant", "content": "다시 한번 말해주세요."})
            elif len(text) < 3:
                st.session_state[familymsg].append({"role":"assistant", "content": "다시 한번 말해주세요."})   
            else:
                chat(text)

with row1:
    if st.session_state[familyfirst] == True:
        user_turn = {"role":"user", "content": familyfirstmsg}
        resp = requests.post(chat_url, json={"messages": [user_turn]})
        assistant_turn = resp.json()

        st.session_state[familymsg].append(assistant_turn)

        msg = assistant_turn['content']

        message(msg, is_user=False, key=f"chat_00")

        st.session_state[familyfirst] = False
    else:
        # length = len(st.session_state[familymsg]) ## 음성합성

        for i, msg_obj in enumerate(st.session_state[familymsg]):
                if msg_obj['role'] == 'img':
                    url = msg_obj['content']
                    if "실패" not in url:
                        message(f'<img width="100%" height="256" src="{url}"/>', is_user=False, key=f"chat_{i}", allow_html=True)

                else:    

                    msg = msg_obj['content'].replace('\"', '')
                    role = msg_obj['role']

                    is_user = True
                    if role == "assistant":
                        is_user = False
                    
                    message(msg, is_user=is_user, key=f"chat_{i}")

                    ## 음성 합성
                    # if i == length - 1:
                    #     message(msg, is_user=is_user, key=f"chat_{i}")
                    # else:
                    #     message(msg, is_user=is_user, key=f"chat_{i}")
