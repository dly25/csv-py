def age_data(data):
    from terminal import terminal_data

    try:
        inp = input("Хотите узнать person по возрасту файл?(yes/no): ")
        if not inp in ("no", "#"):
            sorted_data = sorted(data.values(), key=lambda x: x.get("user_age", 0), reverse=True)
            print(sorted_data)
            terminal_data()
        else:
            print()
            terminal_data()
    except ValueError as e:
        print(e)
