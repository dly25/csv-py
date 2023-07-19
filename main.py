import json
def load_data():
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Не найден файл!")
        return {}
    except json.JSONDecodeError:
        print("Что-то не правильно в файле!")
        return {}

def save_data(data):
    with open("data.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))

def show_data(data):
    try:
        inp = input("Введите запрос на показ data (yes/no): ")
        if inp == "yes":
            print(data)
        elif inp == "no":
            print()
        else:
            raise ValueError("НЕ правильный запрос!")
    except ValueError as e:
        print(e)

def change_data(data):
    try:
        inp = input("Хотите изменить файл?(yes/no): ")
        if not inp == "no":
            inp_person, inp_item, inp_change = input("Введите запрос на изменения data пример(person1)"
                                                     "(user_name)(изменения) ").strip().split()
            data[inp_person][inp_item] = inp_change
            save_data(data)
            show_data(data)
        else:
            print()
    except ValueError:
        print("НЕ правильный запрос!")
    except KeyError:
        print("НЕ правильный ключ!")

def filter_data(data):
    try:
        inp = input("Хотите отфильтровать файл?(yes/no): ")
        if not inp == "no":
            inp_filter = input("Введите хотите отфильтровать: ")
            for output in data:
                output_name = data[output].get(inp_filter)
                if output_name:
                    print(output_name)
                else:
                    raise ValueError("НЕ правильный запрос!")
            show_data(data)
        else:
            print()
    except ValueError as e:
        print(e)
    except KeyError:
        print("НЕ правильный ключ!")

def count_data(data):
    try:
        inp = input("Хотите count файл?(yes/no): ")
        if not inp == "no":
            inp_count = input("Введите хотите count: ")
            result = len(data[inp_count])
            print(result)
        else:
            print()
    except ValueError as e:
        print(e)

def main():
    data = load_data()

    save_data(data)
    show_data(data)
    change_data(data)
    filter_data(data)
    count_data(data)

if __name__ == "__main__":
    main()