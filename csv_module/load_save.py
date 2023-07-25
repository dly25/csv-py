import csv
def load_data():
    try:
        with open("data.csv") as file:
            data = file.writer()
            data
    except FileNotFoundError:
        print("Файл не найден!")
    except csv.Error:
        print("Что-то не так с файлом!")

