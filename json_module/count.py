def count_data(data):
    from .terminal import terminal_data

    try:
        inp = input("Хотите count файл?(yes/no): ")
        if inp.lower() in ("yes", "/"):
            inp_count = input("Введите персону от которой хотите count: ")
            result = len(data[inp_count])
            print(result)
            terminal_data()
        elif inp.lower() in ("no", "#"):
            print()
            terminal_data()
    except ValueError as e:
        print(e)
