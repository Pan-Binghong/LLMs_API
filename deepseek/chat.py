#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   chat.py
@Time    :   2024/12/13 14:48:01
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   基于deepseek的api-key, 调用deepseek的模型
'''
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')

client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com/v1")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你好, 你是谁?"},
    ],
    stream=False
)

print(response.choices[0].message.content)
# 你好！我是DeepSeek Chat，一个由深度求索公司开发的智能助手，旨在通过自然语言处理和机器学习技术来提供信息查询、对话交流和解答问题等服务。有什么我可以帮助你的吗？