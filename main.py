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
    data[list(data.keys())[1]]["user_name"] = "Artem"

    with open("data.json", "w") as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))

    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        print(data)
    def filter_name():
        try:
            # Запрос на то что показать
            inp = input("Введите: ")
            # Фильтрация данных и вывод определенных полей (например, только имен пользователей)
            for output in data:
                output_data = data[output].get(inp)
                if output_data:
                    print("Вывод: ", output_data)
                else:
                    raise ValueError
        except ValueError as e:
            print("Не правильный запрос!")

    filter_name()
f()