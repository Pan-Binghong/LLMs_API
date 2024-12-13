#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   model_list.py
@Time    :   2024/12/13 09:46:06
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   View the list of available models.
'''

import os
import http.client
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

conn = http.client.HTTPSConnection("api.chatanywhere.tech")
payload = ''
headers = {
   'Authorization': f'Bearer {openai_api_key}'
}
conn.request("GET", "/v1/models", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))