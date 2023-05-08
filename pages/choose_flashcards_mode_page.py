from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from functions.actions import go_to_create_new_list_page, go_to_menu, go_to_add_word_page


class ChooseFlashcardsMode(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 3
        self.padding = 15
        self.spacing = 15

        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.4)
        self.btn = Button(text='Add flashcards', font_size=20)
        self.btn.bind(on_press=go_to_add_word_page)
        self.mybox.add_widget(self.btn)
        self.add_widget(self.mybox)

        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.4)
        self.btn1 = Button(text='Create new list', font_size=25)
        self.btn1.bind(on_press=go_to_create_new_list_page)
        self.mybox.add_widget(self.btn1)
        self.add_widget(self.mybox)

        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.2)
        self.btn1 = Button(text='Menu', font_size=25)
        self.btn1.bind(on_press=go_to_menu)
        self.mybox.add_widget(self.btn1)
        self.add_widget(self.mybox)
