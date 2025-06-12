import json
with open('company.json','r',encoding='utf-8') as f:
    data = json.load(f)
print(data)