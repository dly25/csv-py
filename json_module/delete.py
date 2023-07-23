def delete_data(data):
    from .terminal import terminal_data
    from .load_save import load_data, save_data

    try:
        inp = input("Хотите удалить часть файла?(yes/no): ")
        if inp.lower() in ("yes", "/"):
            inp_fun, inp_delete = input("Полное удаления или ключ-значения?"
                                     "(full person(1..)/ item user_...): ").strip().split()
            if inp_fun.lower() == "full":
                data_del = data.pop(inp_delete)
                save_data(data)
                print(f"Удаленный {inp_delete}: {data_del}")
                print()
                terminal_data()
        elif inp.lower() in ("no", "#"):
            print()
            terminal_data()
    except ValueError as e:
        print(e)
