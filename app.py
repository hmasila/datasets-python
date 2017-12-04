from main_menu import MainMenu
class App:
    def __init__(self):
        self.menu = MainMenu("Main MENU", ["Quarterbacks", "Running backs", "Receivers", "Tackles", "Interceptions"])

    def run(self):
        self.menu.prompt();

if __name__ == "__main__":
    App().run();
