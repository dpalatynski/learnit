from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from functions.actions import go_to_flashcard, go_to_menu
from functions.functions import find_list_of_flashcards


class ChooseFlashcards(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.flashcards = find_list_of_flashcards('./data/flashcards.json')

        self.rows = 2 + len(self.flashcards)
        self.padding = 15
        self.spacing = 15

        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.1, size_hint_y=None)
        self.lbl = Label(text='Choose flashcards:', font_size=40)
        self.mybox.add_widget(self.lbl)
        self.add_widget(self.mybox)

        for item in self.flashcards:
            self.mybox = BoxLayout(orientation='horizontal')
            self.btn = Button(text=item, font_size=20)
            self.btn.bind(on_press=go_to_flashcard)
            self.mybox.add_widget(self.btn)
            self.add_widget(self.mybox)

        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.1, size_hint_y=None)
        self.btn1 = Button(text='Menu', font_size=25)
        self.btn1.bind(on_press=go_to_menu)
        self.mybox.add_widget(self.btn1)
        self.add_widget(self.mybox)
