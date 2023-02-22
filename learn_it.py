from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
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
        self.word_page = WordPage()
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

        screen = Screen(name="WordPage")  # Flashcard
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
        self.btn1.bind(on_press=self.gotowordpage)
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

    def gotowordpage(self, instance):
        learnit.screen_manager.current = "WordPage"


class WordPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 6
        self.padding = 15
        self.spacing = 15
        self.huge = False   # capital/normal letter in _on_keyboard_down

        # wyswietlanie slowa
        self.words = BoxLayout(orientation = 'horizontal', height = Window.size[1]*0.2, size_hint_y = None)
        self.word = Label(text=words_in_polish[number], font_size=40, color=[128,128,128, 1], halign='left',
                          valign='bottom')
        self.word.bind(size=self.word.setter('text_size'))
        self.words.add_widget(self.word)
        self.add_widget(self.words)

        # roboczy label
        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.05, size_hint_y=None)
        self.grade = Label(text=' ', font_size=20, color=[0,128,0, 1], halign='right', valign='bottom')
        self.grade.bind(size=self.grade.setter('text_size'))
        self.mybox.add_widget(self.grade)
        self.add_widget(self.mybox)

        # wpisywanie odpowiedzi
        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.3, size_hint_y=None)
        self.txt = TextInput(multiline=True, font_size=35, keyboard_mode='managed',  is_focusable=True, focus=True,
                             unfocus_on_touch=False)
        self.txt.keyboard_on_key_down = self._on_keyboard_down
        self.mybox.add_widget(self.txt)
        self.add_widget(self.mybox)

        # przyciski do slowek
        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.1, size_hint_y=None)
        self.btn = Button(text='Podpowiedz litere', font_size=25)
        self.btn1 = Button(text='Sprawdz odpowiedz', font_size=25)
        self.btn1.bind(on_press=self.check_answer)
        self.mybox.add_widget(self.btn)
        self.mybox.add_widget(self.btn1)
        self.add_widget(self.mybox)

        # przyciski funkcyjne
        self.mybox = BoxLayout(orientation='horizontal', height=Window.size[1]*0.1, size_hint_y=None)
        self.btn2 = Button(text='Menu', font_size=25)
        self.btn2.bind(on_press=self.gotomenu)
        self.btn3 = Button(text='Wyjscie', font_size=25)
        self.btn3.bind(on_press=self.exitbutton)
        self.mybox.add_widget(self.btn2)
        self.mybox.add_widget(self.btn3)
        self.add_widget(self.mybox)

        Window.bind(on_key_down=self._on_keyboard_down)


    def _on_keyboard_down(self, *args):
        if args[1] == 276:
            self.txt.cursor = (self.txt.cursor[0]-1, self.txt.cursor[1])
        elif args[1] == 275:
            self.txt.cursor = (self.txt.cursor[0]+1, self.txt.cursor[1])
        elif args[1] == 273:
            self.txt.cursor = (self.txt.cursor[0], self.txt.cursor[1]-1)
        elif args[1] == 274:
            self.txt.cursor = (self.txt.cursor[0], self.txt.cursor[1]+1)
        elif args[2] == 42:
            self.txt.text = self.txt.text[:-1]
        elif args[1] == 303 or args[1] == 304:
            self.huge = True
        elif args[1] == 13:
            self.check_answer()
        elif args[1] == 301:
            pass
        elif args[3] is not None:
            if self.huge is True:
                self.txt.text += args[3].upper()
                self.huge = False
            else:
                self.txt.text += args[3]

    def exitbutton(self, instance):
        App.get_running_app().stop()
        Window.close()

    def gotomenu(self, instance):
        learnit.screen_manager.current = "EntryPage"

    def check_answer(self, instance=None):
        words_in_input = self.txt.text.lower()
        global number
        if words_in_english[number].lower() == words_in_input.strip():
            if self.txt.foreground_color == [0, 0, 0, 1]:
                self.txt.foreground_color = [0, 0.8, 0, 1]
                self.grade.color = [0, 0.8, 0, 1]
                self.grade.text = 'Excellent!'
                self.btn1.text = "Dalej"
            elif self.txt.foreground_color == [0, 0.8, 0, 1] or self.txt.foreground_color == [128, 0, 0, 1]:
                number = random.randrange(0, len(lines))
                self.word.text = words_in_polish[number]
                self.txt.text = ''
                self.grade.text = ' '
                self.txt.foreground_color = [0, 0, 0, 1]
                self.btn1.text = "Sprawdź odpowiedź"
        else:
            self.grade.text = 'Wrong!'
            self.grade.color = [128, 0, 0, 1]
            self.txt.text = words_in_english[number].lower()
            self.txt.foreground_color = [128, 0, 0, 1]
            self.btn1.text = "Dalej"


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

