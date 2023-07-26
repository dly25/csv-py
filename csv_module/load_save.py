import csv
def load_data():
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        print("Файл не найден!")
        return []
    except csv.Error:
        print("Что-то не так с файлом!")
        return []

def save_data(data):
    with open("data.csv", "a") as file:
        data = csv.writer(file)

