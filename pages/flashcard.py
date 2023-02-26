from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from functions.functions import read_json_to_dict
import random

from functions.actions import go_to_menu, close_app


class Flashcard(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 6
        self.padding = 15
        self.spacing = 15
        self.flashcards = read_json_to_dict('./data/flashcards.json')
        self.target_word = random.choice(list(self.flashcards.keys()))
        self.native_word = self.flashcards[self.target_word]
        self.displayed_results = False

        # display a flashcard
        self.words = BoxLayout(orientation='horizontal', height=Window.size[1]*0.2, size_hint_y=None)
        self.word = Label(text=self.native_word, font_size=40, color=(128, 128, 128, 1), halign='left',
                          valign='bottom')
        self.word.bind(size=self.word.setter('text_size'))
        self.words.add_widget(self.word)
        self.add_widget(self.words)

        # display results
        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.05, size_hint_y=None)
        self.grade = Label(text='', font_size=20, color=(0, 128, 0, 1), halign='right', valign='bottom')
        self.grade.bind(size=self.grade.setter('text_size'))
        self.mybox.add_widget(self.grade)
        self.add_widget(self.mybox)

        # entry txt field to write an answer
        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.3, size_hint_y=None)
        self.txt = TextInput(multiline=True, font_size=35, cursor_color=(0, 0, 0, 1))
        self.txt.keyboard_on_key_down = self._on_keyboard_down
        self.mybox.add_widget(self.txt)
        self.add_widget(self.mybox)

        # 1st row of buttons: hint & check
        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.1, size_hint_y=None)
        self.btn1 = Button(text='Hint', font_size=25)
        self.btn2 = Button(text='Check', font_size=25)
        self.btn2.bind(on_press=self.check_answer)
        self.mybox.add_widget(self.btn1)
        self.mybox.add_widget(self.btn2)
        self.add_widget(self.mybox)

        # 2nd row of buttons: go to menu & exit
        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.1, size_hint_y=None)
        self.btn3 = Button(text='Menu', font_size=25)
        self.btn3.bind(on_press=go_to_menu)
        self.btn4 = Button(text='Exit', font_size=25)
        self.btn4.bind(on_press=close_app)
        self.mybox.add_widget(self.btn3)
        self.mybox.add_widget(self.btn4)
        self.add_widget(self.mybox)

        Window.bind(on_key_down=self._on_keyboard_down)
        Clock.schedule_once(self.set_focus, 0.1)

    def set_focus(self, _):
        self.txt.focus = True

    def _on_keyboard_down(self, *args):
        if args[1] == 276:
            self.txt.do_cursor_movement(action='cursor_left')
        elif args[1] == 275:
            self.txt.do_cursor_movement(action='cursor_right')
        elif args[1] == 273:
            self.txt.do_cursor_movement(action='cursor_up')
        elif args[1] == 274:
            self.txt.do_cursor_movement(action='cursor_down')
        elif args[2] == 42:  # backspace
            self.txt.do_backspace()
        elif args[1] == 13 and self.txt.focus is True:  # enter
            self.check_answer()

    def check_answer(self, _=None):
        Clock.schedule_once(self.set_focus, 0.1)
        if self.target_word.lower() == self.txt.text.lower().strip():
            if self.displayed_results is False:
                self.answer_correct()
            elif self.displayed_results is True:
                self.new_flashcard_page()
        else:
            self.answer_wrong()

    def answer_correct(self):
        self.txt.foreground_color = [0, 0.5, 0, 1]
        self.txt.cursor_color = (0.75, 0.75, 0.75, 1)
        self.txt.background_color = (0.75, 0.75, 0.75, 1)
        self.txt.readonly = True
        self.grade.color = [0, 0.8, 0, 1]
        self.grade.text = 'Excellent!'
        self.btn2.text = "Next"
        self.displayed_results = True

    def answer_wrong(self):
        self.grade.text = 'Wrong!'
        self.grade.color = (128, 0, 0, 1)
        self.txt.text = self.target_word
        self.txt.foreground_color = (128, 0, 0, 1)
        self.txt.background_color = (0.75, 0.75, 0.75, 1)
        self.txt.readonly = True
        self.txt.cursor_color = (0.75, 0.75, 0.75, 1)
        self.btn2.text = "Next"
        self.displayed_results = True

    def new_flashcard_page(self):
        self.new_flashcard()
        self.word.text = self.native_word
        self.txt.readonly = False
        self.txt.cursor_color = (0, 0, 0, 1)
        self.txt.text = ''
        self.grade.text = ' '
        self.txt.foreground_color = (0, 0, 0, 1)
        self.txt.background_color = (0.99, 0.99, 0.99, 1)
        self.btn2.text = "Check"
        self.displayed_results = False

    def new_flashcard(self):
        self.target_word = random.choice(list(self.flashcards.keys()))
        self.native_word = self.flashcards[self.target_word]
