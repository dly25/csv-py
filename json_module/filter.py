def filter_data(data):
    from terminal import terminal_data

    try:
        inp = input("Хотите отфильтровать файл?(yes/no): ")
        if not inp in ("no", "#"):
            inp_filter = input("Введите хотите отфильтровать: ")
            for output in data:
                output_name = data[output].get(inp_filter)
                if output_name:
                    print(output_name)
                    terminal_data()
                else:
                    raise ValueError("НЕ правильный запрос!")
        else:
            print()
            terminal_data()
    except ValueError as e:
        print(e)
    except KeyError:
        print("НЕ правильный ключ!")
