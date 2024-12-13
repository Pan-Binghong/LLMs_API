#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   glm-4v-flash.py
@Time    :   2024/12/13 14:26:53
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   使用免费的智谱AI模型, 调用glm4-v-flash模型
'''

import os
from zhipuai import ZhipuAI
from dotenv import load_dotenv

load_dotenv()

zhipuai_api_key = os.getenv('ZHIPU_API_KEY')

client = ZhipuAI(api_key=zhipuai_api_key)

response = client.chat.completions.create(
    model="glm-4v-flash",
    messages=[
        {"role": "user", "content": [
            {"type": "text", "text": "请描述一下图片上有什么?"},
            {"type": "image_url", "image_url": {
                "url": "https://raw.githubusercontent.com/Pan-Binghong/SuanliTuiJian-v2_mini-programme/refs/heads/main/static/ai-avatar.png"
            }}
        ]}
    ]
)

print(response.choices[0].message.content)
"""
这张图片展示了一个卡通风格的柴犬头像表情符号。

这个表情符号的设计简洁而富有表现力：
- 它有一个圆润的头和尖尖的耳朵；
- 狗的眼睛很大很有神，一只眼睛半闭着，给人一种轻松或疲倦的感觉；
- 鼻子小小的，嘴巴微笑着，显得友好和亲切；
- 整个表情符号以黄色为主色调，线条清晰，轮廓分明。

总的来说，这个表情符号非常可爱，能够很好地传达出狗狗的快乐情绪。
"""