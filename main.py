import json
def load_data():
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Не найден файл!")
    except json.JSONDecodeError:
        print("Что-то не правильно в файле!")

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
        inp_person, inp_item, inp_change = input("Введите запрос на изменения data пример(person1)(user_name)(изменения) ").strip().split()
        data[inp_person][inp_item] = inp_change
        save_data(data)
        show_data(data)
    except ValueError:
        print("НЕ правильный запрос!")
    except KeyError:
        print("НЕ правильный ключ!")

def main():
    data = load_data()

    save_data(data)
    show_data(data)
    change_data(data)

if __name__ == "__main__":
    main()