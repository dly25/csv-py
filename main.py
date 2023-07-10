import json
def f():
    # Данные которые добавляем в json
    data = {
        "user_name": "Anton",
        "user_age": 35,
        "user_email": "aaa@gmail.com"
    }
    # Создания файла Json
    with open("data.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))
f()