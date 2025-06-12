你提供的是一个典型的 JSON 数组，每个元素是一个用户信息字典。你要**取出每个用户的地址**，可以使用如下方法：

---

### ✅ 假设这个数据被加载为 `users`（是一个列表）：

```python
import json

# 假设 users 是你从文件或接口中加载的数据
# users = json.load(f) 或 users = response.json()

for user in users:
    address = user["address"]
    print(f"{user['name']} 的地址：")
    print(f"  街道: {address['street']}")
    print(f"  套间: {address['suite']}")
    print(f"  城市: {address['city']}")
    print(f"  邮编: {address['zipcode']}")
    print(f"  经纬度: {address['geo']['lat']}, {address['geo']['lng']}")
    print()  # 换行
```

---

### 🧾 示例输出：

```
Leanne Graham 的地址：
  街道: Kulas Light
  套间: Apt. 556
  城市: Gwenborough
  邮编: 92998-3874
  经纬度: -37.3159, 81.1496

Ervin Howell 的地址：
  街道: Victor Plains
  套间: Suite 879
  城市: Wisokyburgh
  邮编: 90566-7771
  经纬度: -43.9509, -34.4618
```

---

### 💡 提示：

你也可以只提取某些字段，例如只要城市和经纬度：

```python
for user in users:
    city = user["address"]["city"]
    geo = user["address"]["geo"]
    print(f"{user['name']} - 城市: {city}，坐标: ({geo['lat']}, {geo['lng']})")
```

---

是否希望我帮你把所有用户的地址整理成表格形式（如 pandas DataFrame）？这对于批量数据分析非常方便。
