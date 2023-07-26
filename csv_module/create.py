def create_data(data):
    from .terminal import terminal_data
    from load_save import save_data

    try:
        inp = input("Хотите добавить новую персону?(yes/no): ").lower()

    except ValueError as e:
        print(e)
