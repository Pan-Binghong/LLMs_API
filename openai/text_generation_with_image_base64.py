#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   text_generation_with_image_base64.py
@Time    :   2024/12/13 11:17:05
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   上传base64编码的图片, 进行文本生成
'''

import os
import base64
from openai import OpenAI
from dotenv import load_dotenv

# 定义函数, 将图片转换为base64编码
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# 图片路径
image_path = "openai/test_img_audio/image.jpg"

# 将图片转换为base64编码
image_base64 = encode_image(image_path)

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

model = "gpt-4o-mini"

client = OpenAI(api_key=openai_api_key, base_url="https://api.chatanywhere.tech/v1")

completion = client.chat.completions.create(
    model=model,
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "图片上有什么?"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
            ]
        }
    ],
    max_tokens=300
)

print(completion.choices[0].message.content)
# 图片上有一个可爱的卡通兔子，穿着一件黄色雨衣，雨衣有帽子，虽然外面在下雨。背景是阴云密布的天气，增加了雨天的感觉。兔子看起来很友好，站在雨中。