from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '650')

calc_str = ""
shift = False
alpha = False


class Normal(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception as e:
                print(e)
                self.display.text = "Error"


class CalculatorApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Normal(name="normal"))
        sm.add_widget()
        return sm


if __name__ == "__main__":
    CalculatorApp().run()

