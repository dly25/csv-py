def sort_data(data):
    from .terminal import terminal_data

    try:
        inp = input("Хотите отсортировать файл?(yes/no): ")
        if not inp.lower() in ("no", "#"):
            inp_that, inp_order = input("Что хотите отсортировать и в каком порядке пример"
                        "(user_age (1/0) / no): ").strip().split()
            if not inp_that == "no":
                sorted_data = sorted(
                    data.values(),
                    key=lambda x: x.get(inp_that, 0),
                    reverse=bool(inp_order)
                    )
                print(sorted_data)
                print("\n")
                terminal_data()
        else:
            print("\n")
            terminal_data()
    except ValueError as e:
        print(e)
