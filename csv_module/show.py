def show_data(data):
    from .terminal import terminal_data

    try:
        inp = input("Хотите увидеть файл?(yes/no): ").lower()
        if inp in ("yes", "/"):
            for show in data:
                print(show)
            print()
            terminal_data()
        elif inp in ("no", "#"):
            print()
            terminal_data()
    except ValueError as e:
        print(e)
