from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MainScreen(BoxLayout):
    pass

class PeguedexApp(App):
    title = "PEGUEDEX"
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    PeguedexApp().run()
