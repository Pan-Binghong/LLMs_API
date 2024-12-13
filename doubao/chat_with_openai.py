from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

enpotion_id = "ep-20241120093143-kj6vt"

client = OpenAI(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=os.environ.get("DOUBAO_API_KEY")
)

completion = client.chat.completions.create(
    model=enpotion_id,
    messages = [
        # {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
        {"role": "user", "content": "你好, 你是谁?"},
    ],
)

print(completion.choices[0].message.content)
# 你好！我是豆包，能回答各种各样的问题并进行交流，很高兴能和你聊天！