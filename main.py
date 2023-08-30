import kivy
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior

class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass
class CareScreen(Screen):
    pass
class ImageButton(ButtonBehavior, Image):
    pass 
GUI = Builder.load_file('kv/my.kv')
class MyApp(App):
    def build(self):
        return GUI
    def change_screen(self, screenName):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.transition
        screen_manager.current = screenName

        

if __name__ == "__main__":
    MyApp().run()
