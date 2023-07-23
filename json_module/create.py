def create_data(data):
    from .terminal import terminal_data
    from .load_save import save_data, load_data, sorted_data

    try:
        inp = input("Хотите создать новую часть файла?(yes/no): ")
        if not inp.lower() in ("no", "#"):
            inp_person = input("1. Персона пример(person...): ").strip()
            inp_user_name_value = input("2. Имя пользователя пример(Anton): ").strip()
            inp_user_age_value = input("2. Возраст пользователя пример(20): ").strip()
            inp_user_email_value = input("2. Email пользователя пример(www@gmail.com): ").strip()
            inp_user_name_key = "user_name"
            inp_user_age_key = "user_age"
            inp_user_email_key = "user_email"

            if inp_person in data:
                print()
                terminal_data()
            else:
                data[inp_person] = {
                    inp_user_name_key: inp_user_name_value,
                    inp_user_age_key: int(inp_user_age_value),
                    inp_user_email_key: inp_user_email_value,
                }
                print("Создалась часть файла!")
                save_data(data)
                print()
                terminal_data()
                return data


    except ValueError as e:
        print(e)
        print()
        terminal_data()
