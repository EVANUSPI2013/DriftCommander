import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class DriftCommander(toga.App):
    def startup(self):
        # Main layout box - Horizontal (Left button | Right button)
        main_box = toga.Box(style=Pack(direction=ROW, padding=20))

        # Left Motor Button
        # Sends 'L' when pressed, 'S' when released
        self.left_btn = toga.Button(
            'LEFT TRACK',
            on_press=self.send_left,
            on_release=self.send_stop,
            style=Pack(flex=1, padding=10, height=200)
        )

        # Right Motor Button
        # Sends 'R' when pressed, 'S' when released
        self.right_btn = toga.Button(
            'RIGHT TRACK',
            on_press=self.send_right,
            on_release=self.send_stop,
            style=Pack(flex=1, padding=10, height=200)
        )

        main_box.add(self.left_btn)
        main_box.add(self.right_btn)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def send_left(self, widget):
        print("L")  # This will be picked up by the Bluetooth module

    def send_right(self, widget):
        print("R")

    def send_stop(self, widget):
        print("S")

def main():
    return DriftCommander()
