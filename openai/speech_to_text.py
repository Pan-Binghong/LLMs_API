#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   speech_to_text.py
@Time    :   2024/12/13 13:55:44
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   "使用openai提供的whisper-1模型进行语音转文字"
'''


import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

audio_file = open("openai/test_img_audio/audio.mp3", "rb")

client = OpenAI(api_key=openai_api_key, base_url="https://api.chatanywhere.tech/v1")

transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)
print(transcription.text)
# 請你解釋一下 什麼是深拷貝和淺拷貝