import json
with open('company.json','r',encoding='utf-8') as f:
    data = json.load(f)

# 美观输出
print(json.dumps(data,indent=4,ensure_ascii=False))

# print(json.dumps(data['departments'],indent=4,ensure_ascii=False))

for dept in data['departments']:
    for emp in dept['employees']:
        print(emp['name'],emp['id'],emp['age'],end=" ")
        for skill in emp['skills']:
            print(skill,end=" ")
        print() # 打印完一行后换行（不是空行）