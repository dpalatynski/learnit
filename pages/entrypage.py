from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from functions.actions import go_to_add_choose_page, go_to_flashcard, go_to_setting_page, close_app


class EntryPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 3
        self.padding = 15
        self.spacing = 15

        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.35)
        self.lbl = Label(text='Learn it!', font_size=40)
        self.mybox.add_widget(self.lbl)
        self.add_widget(self.mybox)

        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.35)
        self.btn = Button(text='Add flashcards', font_size=25)
        self.btn.bind(on_press=go_to_add_choose_page)
        self.btn1 = Button(text='Start', font_size=25)
        self.btn1.bind(on_press=go_to_flashcard)
        self.mybox.add_widget(self.btn)
        self.mybox.add_widget(self.btn1)
        self.add_widget(self.mybox)

        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.30)
        self.btn = Button(text='Settings', font_size=25)
        self.btn.bind(on_press=go_to_setting_page)
        self.btn1 = Button(text='Exit', font_size=25)
        self.btn1.bind(on_press=close_app)
        self.mybox.add_widget(self.btn)
        self.mybox.add_widget(self.btn1)
        self.add_widget(self.mybox)
