from typing import List
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
app = FastAPI()

def chat(messages):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    resp_dict = response.to_dict_recursive()
    assistant_turn = resp_dict['choices'][0]['message']

    return assistant_turn

class Turn(BaseModel):
    role: str
    content: str

class Messages(BaseModel):
    messages: List[Turn]


@app.post("/chat")
def post_chat(messages: Messages):
    messages = messages.dict()
    assistant_turn = chat(messages=messages['messages'])
    return assistant_turn

@app.post("/stt")
def stt(audio_file: UploadFile = File(...)):

    try:

        file_name = "tmp_audio_file.wav"
        with open(file_name, "wb") as f:
            f.write(audio_file.file.read())
        
        with open(file_name, "rb") as f:
            text = openai.Audio.transcribe("whisper-1", f)

        text = text['text']

    except Exception as e:
        print(e)
        text = f"음성인식이 실패했습니다. {e}"
    
    return {"text": text}