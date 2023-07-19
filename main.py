import json
def f():
    # Данные которые добавляем в json
    data = {
        "person1": {
            "user_name": "Anton",
            "user_age": 35,
            "user_email": "aaa@gmail.com"
        },
        "person2": {
            "user_name": "Anton",
            "user_age": 35,
            "user_email": "aaa@gmail.com"
        }
    }
    # Создания файла Json
    with open("data.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))
    # Показ данных JSON файла
    with open("data.json", encoding="utf-8") as file:
        data = json.load(file)
        print(data)

    # Изменения JSON файла
    data[list(data.keys())[0]]["user_name"] = "artem"

    with open("data.json", "w") as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))

    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        print(data)
        
    def count_data(data):
        try:
            inp = input("Введите запрос: ")

            result = len(data[inp])

            print(result)
        except ValueError as e:
            print("НЕ правильный запрос")

    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        count_data(data)

if __name__ == "__main__":
    f()