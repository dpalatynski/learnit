from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from functions.actions import go_to_menu


class CreateNewList(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 2

        self.lbl = Label(text='In Progress', font_size=15)
        self.add_widget(self.lbl)

        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.2)
        self.btn1 = Button(text='Menu', font_size=25)
        self.btn1.bind(on_press=go_to_menu)
        self.mybox.add_widget(self.btn1)
        self.add_widget(self.mybox)
