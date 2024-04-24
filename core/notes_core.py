from modules import load, read_notes, menu, add_notes
from templates import cui

def run():
   # load.boot()
    read_notes.open_user_data()

    while True:
        menu.main_menu()
        match cui.select_main_menu():
            case 1:
                add_notes.add_note()
            case 2:
                print("открыть")
            case 3:
                print("поиск")

            case 4:
                print("выгрузить")



