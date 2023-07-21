def filter_data(data):
    from .terminal import terminal_data

    try:
        inp = input("Хотите отфильтровать файл?(yes/no): ")
        if not inp.lower() in ("no", "#"):
            inp_filter = input("Введите что хотите отфильтровать: ")
            for key, value in data.items():
                if inp_filter in value:
                    print(f"{key}: {value[inp_filter]}")
            else:
                raise ValueError("НЕ правильный запрос!")
            print("\n")
            terminal_data()
        else:
            print("\n")
            terminal_data()
    except ValueError as e:
        print(e)
    except KeyError:
        print("НЕ правильный ключ!")
