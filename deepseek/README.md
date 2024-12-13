# OpenAI的API接口使用说明

## 将openai的api密钥导入到环境变量中
  
> 分linux和windows

### Linux

- 在终端中输入以下命令：
  
    ```bash
    export DEEPSEEK_API_KEY=your_api_key
    ```

### Windows
- 在命令提示符中输入以下命令：
    ```bash
    setx DEEPSEEK_API_KEY "your_api_key_here"
    ```

---

### 修改Openai中的base_url

- 在Openai的Python SDK中，修改base_url为deepseek的API地址

    ```python
    client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com/v1")
    ```
