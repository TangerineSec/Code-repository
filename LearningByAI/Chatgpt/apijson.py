
# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/users")
# users = response.json()
# print(users[0]["name"])

import requests
import json
response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()
#print(users[2])
print(json.dumps(users[2],indent=4,ensure_ascii=False))
print("your name：")
for username in users:
    print(username["name"],end= " ")
print("your email")
for username in users:
    print(username["email"],end= " ")
print()
print("your address")
for username in users:
    address = username["address"]
    companyname= username['company']['name']
    print(username['name'],end=" | ")
    print(username['phone'],end=" | ")
    print(username['website'],end=" | ")
    print(address['street'],end=" | ")
    print(companyname,end=" | ")
    print("("+address['geo']['lat']+","+address['geo']['lng']+")")
        # print(addresses["street"],addresses["suite"],addresses["city"],addresses["zipcode"])