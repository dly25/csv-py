def filter_data(data):
    from .terminal import terminal_data

    try:
        inp = input("Хотите отфильтровать файл?(yes/no): ")
        if inp.lower() in ("yes", "/"):
            inp_filter = input("Введите что хотите отфильтровать: ")
            for key, value in data.items():
                if inp_filter in value:
                    print(f"{key}: {value[inp_filter]}")
            else:
                raise ValueError("НЕ правильный запрос!")
        elif inp.lower() in ("no", "#"):
            print()
            terminal_data()
    except ValueError as e:
        print(e)
        print()
        terminal_data()
    except KeyError:
        print("НЕ правильный ключ!")
        print()
        terminal_data()
