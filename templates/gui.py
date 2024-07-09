
# Функция запроса пункта меню у пользователя

def select_main_menu():

    global item_main_menu
    try:
        item_main_menu = int(input("Выберите пункт меню от 1 до 4: "))
    except ValueError:
        print("Пожалуйста, вводите только числа от 1 до 4")

    return item_main_menu

def select_sec_menu():

    global item_sec_menu
    try:
        item_sec_menu = int(input("Выберите пункт меню 1 или 2: "))
    except ValueError:
        print("Пожалуйста, вводите только числа 1 или 2")

    return item_sec_menu

# Запрашиваем данные о новой заметке

def input_data():
    global rating_notes
    try:
        name_notes = input("Название заметки: ")
        description_notes = input("Содержание заметки: ")
        rating_notes = int(input("Выберите уровень важности: 1. Важно, 2. Обычно, 3. Не важно: "))

    except ValueError:
        print("Пожалуйста, вводите только числа от 1 до 3")
    if rating_notes < 1 or rating_notes > 3:
        print("Пожалуйста, вводите число от 1 до 3")
    else:
        if rating_notes > 2:
            rating_notes = "Не важно"
        elif rating_notes < 2:
            rating_notes = "Важно"
        else:
            rating_notes = "Обычно"
    return user_data


