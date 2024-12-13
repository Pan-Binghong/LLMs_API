#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Text_Generation.py
@Time    :   2024/12/13 08:51:18
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   文本生成API调用方式
'''

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

model_name = "gpt-3.5-turbo-ca" # 查看可用模型, 运行model_list.py

client = OpenAI(
    api_key=openai_api_key, 
    base_url="https://api.chatanywhere.tech/v1"
)

completion = client.chat.completions.create(
    model = model_name,
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "你是谁?"
        }
    ]
)

print(completion.choices[0].message.content)
