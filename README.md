# 大模型接口调用示例

![logo](./assets/mylogo.jpg)

本项目集成了各种主流大语言模型的API调用示例代码，帮助开发者快速接入不同的AI模型服务。

## 项目结构
```bash
LLMs_API
├─deepseek
├─doubao
├─langchain
├─llamaindex
├─ollama
├─openai
├─qwen
├─vllm
├─wenxin
├─xinference
└─zhipu
```

## 通用环境变量

- dotenv使用方法

    ```python
    from dotenv import load_dotenv
    import os

    # 加载 .env 文件
    load_dotenv()

    # 获取 API 密钥
    openai_api_key = os.getenv('OPENAI_API_KEY')
    google_api_key = os.getenv('GOOGLE_API_KEY')

    # 打印测试
    print(openai_api_key)
    ```
