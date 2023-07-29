def delete_data(data):
    from .terminal import terminal_data
    from .load_save import load_data, save_data

    try:
        inp = input("Хотите удалить персону?(yes/no): ").lower()
        if inp in ("yes", "/"):
            inp_delete = input("Какую персону хотите удалить? пример(person1): ")
            updated_data = [row for row in data if row["Person"] != inp_delete]
            data = updated_data
            save_data(data)
            print(f"Персона '{inp_delete}' успешно удалена.")
            print()
            terminal_data()
        elif inp in ("no", "#"):
            print()
            terminal_data()
    except ValueError:
        print("Ошибка!!!")