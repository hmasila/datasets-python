from menu import Menu
from statistics_reader import read, retrieve_statistics

class QbMenu(Menu):
    data = read("data_files/QB.txt")

    def option_1(self):
        print(retrieve_statistics(self.data, 3, "completions"))
        self.process_menu_selections()

    def option_2(self):
        print(retrieve_statistics(self.data, 4, "attempts"))
        self.process_menu_selections()

    def option_3(self):
        print(retrieve_statistics(self.data, 7, "yards"))
        self.process_menu_selections()

    def option_4(self):
        print(retrieve_statistics(self.data, 10, "touchdowns"))
        self.process_menu_selections()

    def option_5(self):
        print(retrieve_statistics(self.data, 11, "interceptions"))
        self.process_menu_selections()

    def option_6(self):
        self.parent_menu.prompt()

    def menu_actions(self):
        return {
            '1': self.option_1,
            '2': self.option_2,
            '3': self.option_3,
            '4': self.option_4,
            '5': self.option_5,
            '6': self.option_6
        }
