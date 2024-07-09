from datetime import date
# Функция запроса пункта меню у пользователя

def select_main_menu():

    global item_main_menu
    try:
        item_main_menu = int(input("Выберите пункт меню от 1 до 8: "))
    except ValueError:
        print("Пожалуйста, вводите только числа от 1 до 8")

    return item_main_menu


# Запрашиваем данные о новой заметке

def input_data():
    name_notes = input("Название заметки: ")
    description_notes = input("Содержание заметки: ")
    rating_notes = int(input("Выберите уровень важности: 1. Важно, 2. Обычно, 3. Не важно: "))
    current_date = str(date.today())

    if 1 < rating_notes > 3:
        print("Пожалуйста, вводите число от 1 до 3")
    else:
        if rating_notes > 2:
            rating_notes = "Не важно"
        elif rating_notes < 2:
            rating_notes = "Важно"
        else:
            rating_notes = "Обычно"

    list_data = [name_notes, description_notes, rating_notes, current_date]


    return list_data

def checking_line():
    check_line = int(input("Укажите номер заметки: "))
    check_line -= 1

    return check_line
