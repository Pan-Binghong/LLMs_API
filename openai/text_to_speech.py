#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   text_to_speech.py
@Time    :   2024/12/13 13:57:17
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   使用openai提供的tts模型进行文本转语音
'''

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=openai_api_key, base_url="https://api.chatanywhere.tech/v1")


# 使用 with_streaming_response 方法替代
speech_response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="什么是自回归模型?"
)

with open("openai/test_img_audio/tts_audio.mp3", "wb") as file:
    for chunk in speech_response.iter_bytes():
        file.write(chunk)
