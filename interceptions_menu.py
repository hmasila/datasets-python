from menu import Menu
from statistics_reader import read, retrieve_statistics

class InterceptionsMenu(Menu):
    data = read("data_files/Interceptions.txt")

    def option_1(self):
        print(retrieve_statistics(self.data, 3, "interceptions"))
        self.process_menu_selections()

    def option_2(self):
        self.parent_menu.prompt()

    def menu_actions(self):
        return {
            '1': self.option_1,
            '2': self.option_2
        }
