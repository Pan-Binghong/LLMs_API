#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   chat.py
@Time    :   2024/12/13 16:23:46
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   
'''

import os
from volcenginesdkarkruntime import Ark
from dotenv import load_dotenv

load_dotenv()

client = Ark(api_key=os.environ.get("DOUBAO_API_KEY"))

enpotion_id = "ep-20241120093143-kj6vt"

completion = client.chat.completions.create(
    model=enpotion_id,
    messages=[
        # {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
        {"role": "user", "content": "你好, 你是谁?"},
    ],
)
print(completion.choices[0].message.content)