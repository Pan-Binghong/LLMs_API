#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   text_generation_with_image_url.py
@Time    :   2024/12/13 10:12:15
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   多模态文本生成API调用方式
'''
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

model = "gpt-4o-mini"
client = OpenAI(api_key=openai_api_key, base_url="https://api.chatanywhere.tech/v1")

completion = client.chat.completions.create(
    model=model, 
    messages= [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "图片上有什么?"}, 
                {"type": "image_url", "image_url": {
                    "url": "https://raw.githubusercontent.com/Pan-Binghong/SuanliTuiJian-v2_mini-programme/refs/heads/main/static/ai-avatar.png"
                }
                }
            ]

        }
    ],
    max_tokens=300
)

print(completion.choices[0].message.content)
# 这是一只卡通风格的狗头，通常与“狗狗币”（Dogecoin）有关。它的表情显得俏皮且友好。
