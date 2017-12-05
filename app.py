from main_menu import MainMenu
from statistics_reader import menu_options_dict
class App:
    def __init__(self):
        menu_options = menu_options_dict()
        self.menu = MainMenu(menu_options["main"][0], menu_options["main"][2:])

    def run(self):
        self.menu.prompt();

if __name__ == "__main__":
    App().run();
