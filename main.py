import json
def f():
    # Данные которые добавляем в json
    data = {
        "user_name": "Anton",
        "user_age": 35,
        "user_email": "aaa@gmail.com"
    }
    # Создания файла Json
    with open("data.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))
    # Показ данных JSON файла
    with open("data.json", encoding="utf-8") as file:
        data = json.load(file)
        print(data)

    # Изменения JSON файла
    data["user_name"] = "Artem"

    with open("data.json", "w") as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))

    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        print(data)
f()