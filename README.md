<img src="https://github.com/NahyeonKang/upmentia/assets/24906028/0b2d5c53-e922-44a6-867c-54047b974341" width="300" height="300"/>  


# Upmentia
```
Generative AI를 활용한 치매 회상치료 프로그램입니다.  
```

![Upmentia (2)](https://github.com/NahyeonKang/upmentia/assets/24906028/0f79e953-a15c-42fd-bc37-a929cf420ecc)  


대화상대와 주제를 선택하는 웹페이지  


![Upmentia (3)](https://github.com/NahyeonKang/upmentia/assets/24906028/0053cd20-0e3f-4923-b727-59d69ac65355)  


![Upmentia (4)](https://github.com/NahyeonKang/upmentia/assets/24906028/2fbf825e-6da9-471c-a4fb-40c1bf5db896)   


대화 내용 및 생성 이미지를 보여주는 웹페이지  


![Upmentia (5)](https://github.com/NahyeonKang/upmentia/assets/24906028/9cf368e7-c905-4e35-9ff3-b954fac566ff)  


사용자는 직접 타이핑하거나 음성으로 대화할 수 있습니다. 

---

![1-2](https://github.com/NahyeonKang/upmentia/assets/24906028/fc1f62e1-83fd-4670-91ee-6ad6b2c62187)  


사용자가 주제를 선택하면  


![2 drawio](https://github.com/NahyeonKang/upmentia/assets/24906028/f132e124-0b67-424d-aa7f-a939c423beee)  


GPT가 주제에 맞는 첫 질문을 생성합니다.  


![3](https://github.com/NahyeonKang/upmentia/assets/24906028/c9087299-9f32-4759-bf29-10d1de8291f8)  


사용자가 질문에 대하여 음성으로 답변을 하면 Whisper가 텍스트로 변환합니다.  


![4 drawio](https://github.com/NahyeonKang/upmentia/assets/24906028/c8f9ed26-8276-4481-9bf2-aecd1cd0af82)  


변환된 텍스트 혹은 사용자가 입력한 텍스트는 GPT에 전달되어 답변에 대한 반응과 꼬리질문을 생성합니다.  


![5 drawio](https://github.com/NahyeonKang/upmentia/assets/24906028/91f7071f-2d51-4ff1-af9d-95cf29534621)  

동시에 Dall-E가 보다 정확한 이미지를 생성할 수 있도록 같은 텍스트가 GPT로 전달되어 영어로 번역된 후  Dall-E Prompt를 생성합니다. 해당 Prompt는 Dall-E로 입력되어 사용자의 답변을 묘사하는 이미지를 생성합니다.
