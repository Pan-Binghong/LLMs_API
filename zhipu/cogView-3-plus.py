#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   cog4-view.py
@Time    :   2024/12/13 14:26:53
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   使用免费的智谱AI模型, 调用cogView-3-plus模型
'''

import os
from zhipuai import ZhipuAI
from dotenv import load_dotenv

load_dotenv()

zhipuai_api_key = os.getenv('ZHIPU_API_KEY')

client = ZhipuAI(api_key=zhipuai_api_key)

response = client.images.generations(
    model="cogView-3-plus", #填写需要调用的模型编码
    prompt="一个赛博朋克的柴犬头像",
    size="1440x720"
)

print(response.data[0].url)