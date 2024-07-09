from templates import gui
from modules import menu

path = r"modules/user_data.txt"

def create_array_data():
    array_data = []
    array_data.append(gui.input_data())
    return array_data

def write_data_to_file():
    pass

def add_notes():
    with open(path, mode="a", encoding='utf-8') as w_file:
        file_writer = w_file.write(str(create_array_data()) + '\n')

def edit_notes():
    pass

def view_note():
    with open(path, mode="r", encoding='utf-8') as r_file:
        line = r_file.readlines()[gui.checking_line()]
        print(line.replace('[[', '')
                  .replace(']]', '').replace("'", ''), end="")

def view_all_notes():
    k = 1
    with open(path, mode="r", encoding='utf-8') as r_file:
        line = r_file.readline()
        while line != "":
            print("["+str(k)+"] ", line.replace('[[', '')
                  .replace(']]', '').replace("'", ''),  end="")

            k += 1
            line = r_file.readline()

def delete_notes():
    pass


def upload_to_csv():
    pass

def search_notes():
    pass

def load_main_menu():
    while True:
        menu.main_menu()
        match gui.select_main_menu():
            case 1:
                add_notes()

            case 2:
                view_note()

            case 3:
                view_all_notes()

            case 4:
                print("изменить")

            case 5:
                print("поиск")

            case 6:
                print("удалить")

            case 7:

                print("выгрузить")

            case 8:
                break

