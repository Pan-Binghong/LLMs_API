import json
import time

import requests

# 1. 封装 Header，带上 Token
headers = {
    "Content-Type": "application/json",
    "Token"       : "your access token"
}

# 2. 发起算法调用
resp = requests.post(
    url='https://api.deepdataspace.com/v2/task/dinox/detection', # 这里是举例，具体算法路径查看具体API说明
    json=json.dumps({}),
    headers=headers
)
json_resp = resp.json()
print(json_resp)
# {'code': 0, 'data': {'task_uuid': '092ccde4-a51a-489b-b384-9c4ba8af7375'}, 'msg': 'ok'}

# 3. 获取 task_uuid
task_uuid = json_resp["data"]["task_uuid"]

# 4. 轮询任务状态
while True:
    resp = requests.get(f'https://api.deepdataspace.com/v2/task_status/{task_uuid}', headers=headers)
    json_resp = resp.json()
    if json_resp["data"]["status"] not in ["waiting", "running"]:
        break
    time.sleep(1)

if json_resp["data"]["status"] == "failed":
    print(json_resp)
elif json_resp["data"]["status"] == "success":
    print(json_resp)
