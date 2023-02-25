from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import random


Window.size = (600, 400)
f = open("slowka.txt", "r")
lines = f.readlines()
words_in_polish = []
words_in_english = []

for item in lines:
    a,b = item.split('-')
    words_in_english.append(a.strip())
    words_in_polish.append(b[:-1].strip())

global number
number = random.randrange(0, len(lines))


class LearnItApp(App):
    def __init__(self):
        super().__init__()
        self.screen_manager = ScreenManager()
        self.entry_page = EntryPage()
        self.add_choose_page = AddChoosePage()
        self.add_word = AddWord()
        self.create_new_list = CreateNewList()
        self.word_page = Flashcard()
        self.settings = SettingsPage()

    def build(self):
        screen = Screen(name="EntryPage")  # Entry Page
        screen.add_widget(self.entry_page)
        self.screen_manager.add_widget(screen)

        screen = Screen(name="AddChoosePage")  # Adding words menu (add words or create new lists)
        screen.add_widget(self.add_choose_page)
        self.screen_manager.add_widget(screen)

        screen = Screen(name="AddWord")  # Adding words
        screen.add_widget(self.add_word)
        self.screen_manager.add_widget(screen)

        screen = Screen(name="CreateNewList")  # Create new list of words
        screen.add_widget(self.create_new_list)
        self.screen_manager.add_widget(screen)

        screen = Screen(name="Flashcard")  # Flashcard
        screen.add_widget(self.word_page)
        self.screen_manager.add_widget(screen)

        screen = Screen(name="Settings")  # Settings
        screen.add_widget(self.settings)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


class EntryPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 3
        self.padding = 15
        self.spacing = 15

        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.35)
        self.lbl = Label(text='Nauka słówek', font_size=40)
        self.mybox.add_widget(self.lbl)
        self.add_widget(self.mybox)

        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.35)
        self.btn = Button(text='Dodaj slowka', font_size=25)
        self.btn.bind(on_press=self.addchoosepage)
        self.btn1 = Button(text='Start', font_size=25)
        self.btn1.bind(on_press=self.gotoflashcard)
        self.mybox.add_widget(self.btn)
        self.mybox.add_widget(self.btn1)
        self.add_widget(self.mybox)

        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.30)
        self.btn = Button(text='Ustawienia', font_size=25)
        self.btn.bind(on_press=self.settingsbutton)
        self.btn1 = Button(text='Wyjscie', font_size=25)
        self.btn1.bind(on_press=self.exitbutton)
        self.mybox.add_widget(self.btn)
        self.mybox.add_widget(self.btn1)
        self.add_widget(self.mybox)

    def exitbutton(self, instance):
        App.get_running_app().stop()
        Window.close()

    def settingsbutton(self, instance):
        learnit.screen_manager.current = "Settings"

    def addchoosepage(self, instance):
        learnit.screen_manager.current = "AddChoosePage"

    def addword(self, instance):
        learnit.screen_manager.current = "AddWord"

    def gotoflashcard(self, instance):
        Clock.schedule_once(learnit.word_page.set_focus, 0.1)
        learnit.screen_manager.current = "Flashcard"


class Flashcard(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 6
        self.padding = 15
        self.spacing = 15

        # display a flashcard
        self.words = BoxLayout(orientation='horizontal', height=Window.size[1]*0.2, size_hint_y=None)
        self.word = Label(text=words_in_polish[number], font_size=40, color=(128, 128, 128, 1), halign='left',
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
        self.btn3.bind(on_press=self.gotomenu)
        self.btn4 = Button(text='Exit', font_size=25)
        self.btn4.bind(on_press=self.exitbutton)
        self.mybox.add_widget(self.btn3)
        self.mybox.add_widget(self.btn4)
        self.add_widget(self.mybox)

        Window.bind(on_key_down=self._on_keyboard_down)
        Clock.schedule_once(self.set_focus, 0.1)

    def set_focus(self, dt):
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

    def exitbutton(self, instance):
        App.get_running_app().stop()
        Window.close()

    def gotomenu(self, instance):
        learnit.screen_manager.current = "EntryPage"

    def check_answer(self, instance=None):
        words_in_input = self.txt.text.lower()
        Clock.schedule_once(self.set_focus, 0.1)
        global number
        if words_in_english[number].lower() == words_in_input.strip():
            if self.txt.foreground_color == [0, 0, 0, 1]:
                self.txt.foreground_color = [0, 0.8, 0, 1]
                self.txt.background_color = (128, 128, 128, 1)
                self.txt.readonly = True
                self.txt.cursor_color = (1, 1, 1, 1)
                self.grade.color = [0, 0.8, 0, 1]
                self.grade.text = 'Excellent!'
                self.btn2.text = "Next"
            elif self.txt.foreground_color == [0, 0.8, 0, 1] or self.txt.foreground_color == [128, 0, 0, 1]:
                number = random.randrange(0, len(lines))
                self.word.text = words_in_polish[number]
                self.txt.readonly = False
                self.txt.cursor_color = (0, 0, 0, 1)
                self.txt.text = ''
                self.grade.text = ' '
                self.txt.foreground_color = [0, 0, 0, 1]
                self.txt.background_color = (0.5, 0.5, 0.5, 1)
                self.btn2.text = "Check"
        else:
            self.grade.text = 'Wrong!'
            self.grade.color = [128, 0, 0, 1]
            self.txt.text = words_in_english[number].lower()
            self.txt.foreground_color = [128, 0, 0, 1]
            self.txt.background_color = (128, 128, 128, 1)
            self.txt.readonly = True
            self.txt.cursor_color = (1, 1, 1, 1)
            self.btn2.text = "Next"


class AddChoosePage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 3
        self.padding = 15
        self.spacing = 15

        self.mybox = BoxLayout(orientation = 'horizontal', height = Window.size[1]*0.4)
        self.btn = Button(text = 'Dodaj slowka do istniejacej listy', font_size = 20)
        self.btn.bind(on_press = self.addword)
        self.mybox.add_widget(self.btn)
        self.add_widget(self.mybox)

        self.mybox = BoxLayout(orientation = 'horizontal', height = Window.size[1]*0.4)
        self.btn1 = Button(text = 'Utworz nowa liste', font_size = 25)
        self.btn1.bind(on_press = self.createnewlist)
        self.mybox.add_widget(self.btn1)
        self.add_widget(self.mybox)

        self.mybox = BoxLayout(orientation = 'horizontal', height = Window.size[1]*0.2)
        self.btn1 = Button(text = 'Wyjscie', font_size = 25)
        self.btn1.bind(on_press = self.exitbutton)
        self.mybox.add_widget(self.btn1)
        self.add_widget(self.mybox)

    def exitbutton(self, instance):
        App.get_running_app().stop()
        Window.close()

    def addword(self, instance):
        learnit.screen_manager.current = "AddWord"

    def createnewlist(self, instance):
        learnit.screen_manager.current = "CreateNewList"

    def gotomenu(self, instance):
        learnit.screen_manager.current = "EntryPage"


class AddWord(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 2

        self.lbl = Label(text='Prace techniczne', font_size = 15)
        self.add_widget(self.lbl)

        self.mybox = BoxLayout(orientation = 'horizontal', height = Window.size[1]*0.2)
        self.btn1 = Button(text = 'Menu', font_size = 25)
        self.btn1.bind(on_press = self.gotomenu)
        self.mybox.add_widget(self.btn1)
        self.add_widget(self.mybox)

    def gotomenu(self, instance):
        learnit.screen_manager.current = "EntryPage"


class CreateNewList(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 2

        self.lbl = Label(text='Prace techniczne', font_size = 15)
        self.add_widget(self.lbl)

        self.mybox = BoxLayout(orientation = 'horizontal', height=Window.size[1]*0.2)
        self.btn1 = Button(text = 'Menu', font_size = 25)
        self.btn1.bind(on_press = self.gotomenu)
        self.mybox.add_widget(self.btn1)
        self.add_widget(self.mybox)

    def gotomenu(self, instance):
        learnit.screen_manager.current = "EntryPage"


class SettingsPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 2

        self.lbl = Label(text='Prace techniczne', font_size = 15)
        self.add_widget(self.lbl)

        self.mybox = BoxLayout(orientation = 'horizontal', height = Window.size[1]*0.2)
        self.btn1 = Button(text = 'Menu', font_size = 25)
        self.btn1.bind(on_press = self.gotomenu)
        self.mybox.add_widget(self.btn1)
        self.add_widget(self.mybox)

    def gotomenu(self, instance):
        learnit.screen_manager.current = "EntryPage"


learnit = LearnItApp()
learnit.run()
