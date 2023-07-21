def change_data(data):
    from .terminal import terminal_data
    from .load_save import load_data, save_data

    try:
        inp = input("Хотите изменить файл?(yes/no): ")
        if not inp.lower() in ("no", "#"):
            inp_person, inp_item, inp_change = input("Введите запрос на изменения data пример(person1)"
                                                     "(user_name)(изменения) ").strip().split()
            data[inp_person][inp_item] = inp_change
            save_data(data)
            print("\n")
            terminal_data()
        else:
            print("\n")
            terminal_data()
    except ValueError:
        print("НЕ правильный запрос!")
    except KeyError:
        print("НЕ правильный ключ!")
