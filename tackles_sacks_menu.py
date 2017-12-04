from menu import Menu
from statistics_reader import read, retrieve_statistics

class TacklesSacksMenu(Menu):
    data = read("data_files/Tackles.txt")

    def option_1(self):
        print(retrieve_statistics(self.data, 4, "tackles"))
        self.process_menu_selections()

    def option_2(self):
        print(retrieve_statistics(self.data, 5, "assisted"))
        self.process_menu_selections()

    def option_3(self):
        print(retrieve_statistics(self.data, 6, "sacks"))
        self.process_menu_selections()

    def option_4(self):
        self.parent_menu.prompt()

    def menu_actions(self):
        return {
            '1': self.option_1,
            '2': self.option_2,
            '3': self.option_3,
            '4': self.option_4
        }
