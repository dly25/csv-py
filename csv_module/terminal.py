from .load_save import load_data, save_data, sorted_data
from .show import show_data
from .create import create_data
from .delete import delete_data


def terminal_data():
    try:
        data = load_data()

        inp = input("Введите команду(show, create): ").lower()

        if inp == "show":
            show_data(data)
        if inp == "create":
            create_data(data)
            save_data(data)
        if inp == "create":
            delete_data()
        if inp == "sorted":
            sorted_data(data)
            terminal_data()
    except ValueError as e:
        print(e)
