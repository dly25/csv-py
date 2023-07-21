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
