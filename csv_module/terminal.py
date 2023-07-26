from .load_save import load_data, save_data
from .show import show_data
from .create import create_data

def terminal_data():
    try:
        data = load_data()

        inp = input("Введите команду(show, create): ").lower()

        if inp == "show":
            show_data(data)
        if inp == "create":
            create_data(data)
    except ValueError as e:
        print(e)
