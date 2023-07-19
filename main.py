import json
def load_data():
    try:
        with open("data.json", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Файл не найден, создан новый файл..")
        return {}
    except json.JSONDecodeError:
        print("Что-то не правильное в файле")

def save_data(data):
    with open("data.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))

def change_data(data):
    try:
        inp_person, inp_user, inp_change = input("Введите запрос: ").strip().split()
        data[inp_person][inp_user] = inp_change
        save_data()
    except ValueError:
        print("НЕ правильный запрос!")

def filter_name(data):
    try:
        inp = input("Введите: ")
        for output in data:
            output_data = data[output].get(inp)
            if output_data:
                print("Вывод: ", output_data)
            else:
                raise ValueError("Не правильный запрос!")
    except ValueError as e:
        print(e)

def count_data(data):
    try:
        inp = input("Введите запрос: ")
        result = len(data[inp])
        print(result)
    except ValueError:
        print("НЕ правильный запрос")
    except KeyError:
        print("НЕ правильный ключ")

def f():
    data = load_data()
    print(data)

    change_data(data)
    filter_name(data)
    count_data(data)

if __name__ == "__main__":
    f()
