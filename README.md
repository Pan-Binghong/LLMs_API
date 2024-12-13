# LLMs API 调用示例集合

![logo](./assets/mylogo.jpg)

本项目集成了各种主流大语言模型的 API 调用示例代码，帮助开发者快速接入不同的 AI 模型服务。包括文本生成、图像识别、语音转文字等多种功能。

## 功能特性

- 支持多种主流大语言模型 API
  - OpenAI (GPT-3.5/4)
  - 智谱 AI (GLM-4)
  - 百度文心一言
  - 阿里通义千问
  - DeepSeek
  - 豆包 AI
  
- 支持多种任务类型
  - 文本对话生成
  - 图像理解与描述
  - 语音转文字 (Speech-to-Text)
  - 文字转语音 (Text-to-Speech)
  - 多模态理解

## 快速开始

### 1. 环境准备

```bash
# 克隆项目
git clone https://github.com/your-username/LLMs_API.git

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置密钥

在项目根目录创建 `.env` 文件，添加需要使用的模型的 API 密钥：

```bash
# OpenAI
OPENAI_API_KEY=your_api_key

# 智谱AI
ZHIPU_API_KEY=your_api_key

# 百度文心
QIANFAN_Access_Key=your_access_key
QIANFAN_Secret_Key=your_secret_key

# 阿里千问
DASH_API_KEY=your_api_key

# DeepSeek
DEEPSEEK_API_KEY=your_api_key

# 豆包
DOUBAO_API_KEY=your_api_key
```

### 3. 使用示例

#### 文本对话
```python
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "你好!"}
    ]
)
print(response.choices[0].message.content)
```

#### 图像理解
```python
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "描述这张图片"},
                {"type": "image_url", "image_url": "your_image_url"}
            ]
        }
    ]
)
```

## 项目结构

```
LLMs_API/
├── openai/          # OpenAI API 示例
├── zhipu/           # 智谱 AI API 示例
├── qianfan/         # 百度文心 API 示例
├── qwen/            # 阿里千问 API 示例
├── deepseek/        # DeepSeek API 示例
├── doubao/          # 豆包 API 示例
└── requirements.txt # 项目依赖
```

## 模型支持列表

### OpenAI
- gpt-3.5-turbo
- gpt-4
- whisper-1 (语音转文字)
- tts-1 (文字转语音)

### 智谱 AI
- glm-4
- glm-4v-flash (多模态)
- cogView-3-plus (文生图)

### 阿里千问
- qwen-turbo
- qwen-plus
- qwen-max

### 百度文心
- ernie-4.0
- ernie-bot-8k
- ernie-bot-4

## 注意事项

1. 请确保 API 密钥的安全性，不要将其提交到代码仓库
2. 部分模型可能需要配置代理才能访问
3. 建议在使用前先测试 API 的可用性

## 参考文档

- [OpenAI API 文档](https://platform.openai.com/docs)
- [智谱 AI 开发文档](https://open.bigmodel.cn/dev/api)
- [百度文心开发文档](https://cloud.baidu.com/doc/WENXINWORKSHOP/index.html)
- [阿里千问开发文档](https://help.aliyun.com/document_detail/2400395.html)

## License

MIT