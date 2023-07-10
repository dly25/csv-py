import json
def f():
    # Данные которые добавляем в json
    data = {
        "user_name": "Anton",
        "user_age": 35,
        "user_email": "aaa@gmail.com"
    }
    # Создания файла Json
    with open("data.json", "w") as f:
        json.dump(data, f)
f()