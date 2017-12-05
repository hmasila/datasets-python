from menu import Menu
from qb_menu import QbMenu
from rb_menu import RbMenu
from recv_menu import RecvMenu
from tackles_sacks_menu import TacklesSacksMenu
from interceptions_menu import InterceptionsMenu
from statistics_reader import menu_options_dict
import sys

class MainMenu(Menu):
    def __init__(self, name, options):
        menu_options = menu_options_dict()
        Menu.__init__(self, menu_options["main"][0], menu_options["main"][2:])
        self.qb_menu      = QbMenu(menu_options["qb"][0], menu_options["qb"][2:], self)
        self.rb_menu      = RbMenu(menu_options["rb"][0], menu_options["rb"][2:], self)
        self.recv_menu    = RecvMenu(menu_options["recv"][0], menu_options["recv"][2:], self)
        self.tackles_menu = TacklesSacksMenu(menu_options["tackles_sacks"][0], menu_options["tackles_sacks"][2:], self)
        self.interceptions= InterceptionsMenu(menu_options["interceptions"][0], menu_options["interceptions"][2:], self)

    def option_1(self):
        self.qb_menu.prompt()

    def option_2(self):
        self.rb_menu.prompt()

    def option_3(self):
        self.recv_menu.prompt()

    def option_4(self):
        self.tackles_menu.prompt()

    def option_5(self):
        self.interceptions.prompt()

    def option_6(self):
        sys.exit()

    def menu_actions(self):
        return {
            '1': self.option_1,
            '2': self.option_2,
            '3': self.option_3,
            '4': self.option_4,
            '5': self.option_5,
            '6': self.option_6
        }
