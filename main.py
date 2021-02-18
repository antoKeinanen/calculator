from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition


Builder.load_file('calculator.kv')

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '650')

calc_str = ""
shift = False
alpha = False


class Normal(Screen):
    def calculate(self, item, calculation):
        if calculation:
            try:
                item.ids.entry.text = str(eval(calculation))
            except Exception as e:
                print(e)
                item.ids.entry.text = "Error"


class Shift(Screen):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception as e:
                print(e)
                self.display.text = "Error"


class TestApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.transition = NoTransition()
        sm.add_widget(Normal(name="normal"))
        sm.add_widget(Shift(name="shift"))

        return sm


if __name__ == '__main__':
    TestApp().run()
