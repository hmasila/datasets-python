import os
class Menu:
    def __init__(self, name, options, parent_menu = None):
        self.name = name
        self.options = options
        self.parent_menu = parent_menu

    def prompt(self):
        """Display the menu and prompt user for input"""
        self.clear_screen();
        print(self.name)
        print("-" * 30)
        for index, option in enumerate(self.options):
            print(self.option_text(index, option))
        print("-" * 30)
        self.process_menu_selections()

    def process_menu_selections(self):
        selected_option = input("What would you like to do?  ")
        if self.valid_menu_option(selected_option):
            self.menu_actions()[selected_option]()
        else:
            print("'{}' is not a valid menu option".format(selected_option))
            self.process_menu_selections()

    def select(self):
        """select a given menu option"""
        return input("What would you like to do?")

    def option_text(self, option_index, option_name):
        return "{}   {}".format(option_index + 1, option_name)

    def valid_menu_option(self, selected_option):
        """check whether the option entered by the user is valid"""
        try:
            selected_option = int(selected_option)
        except ValueError:
            return False
        return True if 0 < selected_option <= (len(self.options)) else False

    def clear_screen(self):
        # select clear command depending on local OS.
        # 'cls' for windows and 'clear' for all others
        clear_command = "cls" if os.name == "nt" else "clear"
        os.system(clear_command)
