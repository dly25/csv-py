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

    def change_data():
        # Запрос на изменения Data # Изменения JSON файла
        try:
            #inp_person = input("Введите запрос на изменения(Персона): ")
            #inp_user = input("Введите запрос на изменения(User_name, user_age...): ")
            #inp_change = input("Введите запрос на изменения: ")

            # data[inp_person][inp_user] = inp_change

            inp_person, inp_user, inp_change = input("Введите запрос: ").strip().split()

            data[inp_person][inp_user] = inp_change

        except ValueError as e:
            print("НЕ правильный запрос!")

    change_data()
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