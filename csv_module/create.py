def create_data(data):
    from .terminal import terminal_data
    from .load_save import save_data, load_data

    try:
        inp = input("Хотите добавить новую персону?(yes/no): ").lower()
        if inp in ("yes", "/"):
            inp_person_value = input("Введите Персону пример(person1): ").strip()
            inp_name_value = input("Введите Имя пример(Anton): ").strip()
            inp_age_value = input("Введите Возраст пример(18): ").strip()
            inp_email_value = input("Введите Email пример(www@gmail.com): ").strip()

            inp_person_key = "Person"
            inp_name_key = "Name"
            inp_age_key = "Age"
            inp_email_key = "Email"

            new_person = {
                inp_person_key: inp_person_value,
                inp_name_key: inp_name_value,
                inp_age_key: int(inp_age_value),
                inp_email_key: inp_email_value
            }
            data.append(new_person)
            save_data(data)
            print()
            terminal_data()
        elif inp in ("no", "#"):
            print()
            terminal_data()
        else:
            raise ValueError("Не правильный запрос")
    except ValueError as e:
        print(e)
