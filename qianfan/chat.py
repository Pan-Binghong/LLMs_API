#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   chat.py
@Time    :   2024/12/13 16:00:19
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   
'''

import os
from dotenv import load_dotenv
from qianfan import Qianfan

load_dotenv()

client = Qianfan(
    access_key=os.getenv("QIANFAN_Access_Key"),
    secret_key=os.getenv("QIANFAN_Secret_Key"),
)

model_name = "ernie-4.0-8k-latest"

messages = [
    {
        "role": "user",
        "content": "你好, 你是谁?"
    }
]

response = client.chat.completions.create(
    model = model_name,
    messages = messages,
)

print(response.choices[0].message.content)
# 你好，我是文心一言，英文名是ERNIE Bot。我能够与人对话互动，回答问题，协助创作，高效便捷地帮助人们获取信息、知识和灵感。
