# OpenAI的API接口使用说明

> 该仓库下包含OpenAI的API接口使用说明，以及API调用示例。主要有文本生成模型, 视觉模型, 音频模型等。

## 将openai的api密钥导入到环境变量中
  

### Linux

- 在终端中输入以下命令：
  
    ```bash
    export OPENAI_API_KEY=your_api_key
    ```

### Windows
- 在命令提示符中输入以下命令：
    ```bash
    setx OPENAI_API_KEY "your_api_key_here"
    ```

---

## 安装OpenAI的Python SDK

- 在终端中输入以下命令：

    ```bash
    pip install openai
    ```

## 使用第三方代理

- 使用第三方代理，可以提高API的访问速度和稳定性。

    ```python
    base_url = "https://api.chatanywhere.tech/v1"
    ```
