#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   chat.py
@Time    :   2024/12/13 15:05:35
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   基于阿里Qwen的api-key, 调用阿里Qwen的模型
'''
import os
from dashscope import Generation
from dotenv import load_dotenv

load_dotenv()

qwen_api_key = os.getenv('DASH_API_KEY')

model_name = "qwen-turbo"

response = Generation.call(
    api_key=qwen_api_key,
    model=model_name,
    messages=[
        {"role": "user", "content": "你好, 你是谁?"}
    ],
    stream=False,
    result_format="message"
)


print(response.output.choices[0].message.content)


