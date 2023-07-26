import csv
def load_data():
    try:
        with open("data.csv", "r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        print("Файл не найден!")
        return []
    except csv.Error:
        print("Что-то не так с файлом!")
        return []

def save_data(data):
    fieldnames = ["Person", "Name", "Age", "Email"]

    with open("data.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for person in data:
            writer.writerow(person)

