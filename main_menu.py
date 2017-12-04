from menu import Menu
from qb_menu import QbMenu
from rb_menu import RbMenu
from recv_menu import RecvMenu
from tackles_sacks_menu import TacklesSacksMenu
from interceptions_menu import InterceptionsMenu
import sys

class MainMenu(Menu):
    def __init__(self, name, options):
        Menu.__init__(self,"Main MENU", ["Quarterbacks", "Running backs", "Receivers", "Tackles", "Interceptions"])
        self.qb_menu      = QbMenu("QB Menu", ["Completion", "Attempts", "Yards", "Touchdowns", "Interceptions"], self)
        self.rb_menu      = RbMenu("Running Backs Menu", ["Attempts", "Yards", "Touchdowns", "Longest", "Fumbles"], self)
        self.recv_menu    = RecvMenu("Receivers Menu", ["Receptions", "Yards", "Longest", "Touchdowns", "Fumbles"], self)
        self.tackles_menu = TacklesSacksMenu("Tackles/Sacks Menu", ["Tackles", "Assisted", "Sacks"], self)
        self.interceptions= InterceptionsMenu("Interceptions Menu", ["Interceptions"], self)

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
