def show_data(data):
    from .terminal import terminal_data

    try:
        inp = input("Введите запрос на показ data (yes/no): ")
        if inp == "yes":
            print(data)
            terminal_data()
        elif inp in ("no", "#"):
            print()
            terminal_data()
        else:
            raise ValueError("НЕ правильный запрос!")
    except ValueError as e:
        print(e)

