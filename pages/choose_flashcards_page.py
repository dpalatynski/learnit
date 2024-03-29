from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.checkbox import CheckBox

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
        self.mode = 'study_mode'

        self.scroll_layout = ScrollView(bar_width=15, size_hint_y=None, height=Window.size[1]*0.68,
                                        scroll_type=['bars'])
        self.mybox = BoxLayout(orientation='vertical', size_hint_y=None)
        self.mybox.bind(minimum_height=self.mybox.setter('height'))
        for item in self.flashcards:
            self.btn = Button(text=item, font_size=20, size_hint_y=None, height=75)
            self.btn.bind(on_press=_go_to_flashcard)
            self.mybox.add_widget(self.btn)

        self.btn1 = Button(text='Back to menu', font_size=30, size_hint_y=None)
        self.btn1.bind(on_press=go_to_menu)
        self.mybox.add_widget(self.btn1)

        self.add_widget(self.scroll_layout)
        self.scroll_layout.add_widget(self.mybox)

        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.08, size_hint_y=None)
        self.checkbox1 = CheckBox(group='mode', size_hint=(None, 1), allow_no_selection=False)
        self.label1 = Label(text='Quiz mode')
        self.mybox.add_widget(self.checkbox1)
        self.mybox.add_widget(self.label1)

        self.checkbox2 = CheckBox(group='mode', size_hint=(None, 1), allow_no_selection=False)
        self.checkbox2.active = True
        self.label2 = Label(text='Study mode')
        self.mybox.add_widget(self.checkbox2)
        self.mybox.add_widget(self.label2)

        self.add_widget(self.mybox)

    def checkbox_mode(self):
        self.mode = 'quiz_mode' if self.checkbox1.active is True else 'study_mode'

        return self.mode


def _go_to_flashcard(button_text):
    go_to_flashcard(button_text.text)
