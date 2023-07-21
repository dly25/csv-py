def count_data(data):
    from terminal import terminal_data

    try:
        inp = input("Хотите count файл?(yes/no): ")
        if not inp in ("no", "#"):
            inp_count = input("Введите хотите count: ")
            result = len(data[inp_count])
            print(result)
            terminal_data()
        else:
            print()
            terminal_data()
    except ValueError as e:
        print(e)
