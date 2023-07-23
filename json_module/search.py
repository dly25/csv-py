def search_data(data):
    from .terminal import terminal_data

    try:
        inp = input("Хотите найти Персону?(yes/no): ")
        if inp.lower() in ("yes", "/"):
            inp_person = input("Введите Персону пример(person1): ")
            if inp_person in data:
                print(f"{inp_person}: {data[inp_person]}")
                print()
                terminal_data()
            else:
                raise ValueError("Нет такой Персоны!")
        elif inp.lower() in ("no", "#"):
            print()
            terminal_data()
    except ValueError as e:
        print(e)
        print()
        search_data(data)
