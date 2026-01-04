# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, BooleanProperty
from kivy.clock import Clock
import pygame
import serial
import threading

class DriftApp(App):
    def build(self):
        self.icon = 'icon.png'  # This ensures the tank shows in the task switcher
        return RootWidget()

class RootWidget(BoxLayout):
    l_val = NumericProperty(0)
    r_val = NumericProperty(0)
    drifting = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pygame.init()
        pygame.joystick.init()
        self.joystick = None
        self.ser = None

    def scan_joysticks(self):
        pygame.joystick.quit()
        pygame.joystick.init()
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            self.ids.joy_btn.text = f"CON: {self.joystick.get_name()[:10]}"
        else:
            self.ids.joy_btn.text = "NO CONTROLLER"

    def connect_bluetooth(self):
        # On Windows VS Code, use your COM port (e.g., 'COM3')
        # On Android/Nothing Phone, this path changes
        try:
            self.ser = serial.Serial('COM3', 9600, timeout=0.01) 
            self.ids.bt_btn.text = "HC-05 CONNECTED"
        except:
            self.ids.bt_btn.text = "BT FAILED"

    def update(self, dt):
        if self.joystick:
            pygame.event.pump()
            # Mapping: Axis 1 (LY), Axis 3 or 4 (RY)
            ly = self.joystick.get_axis(1)
            ry = self.joystick.get_axis(3) 
            
            self.l_val = -ly if abs(ly) > 0.15 else 0
            self.r_val = -ry if abs(ry) > 0.15 else 0
            self.drifting = self.joystick.get_button(9)

            if self.ser and self.ser.is_open:
                l_s = int((self.l_val + 1) * 127.5)
                r_s = int((self.r_val + 1) * 127.5)
                packet = f"L{l_s:03d}R{r_s:03d}{'D' if self.drifting else 'U'}\n"
                self.ser.write(packet.encode())

class DriftApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    DriftApp().run()
