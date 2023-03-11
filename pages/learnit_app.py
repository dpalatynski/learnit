from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from pages.entrypage import EntryPage
from pages.flashcard import Flashcard
from pages.addchoosepage import AddChoosePage
from pages.addword import AddWord
from pages.createnewlistpage import CreateNewList
from pages.settingspage import SettingsPage
from pages.choose_flashcards_page import ChooseFlashcards


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
        self.choose_flashcards_page = ChooseFlashcards()

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

        screen = Screen(name="ChooseFlashcards")  # Choose flashcards to learn
        screen.add_widget(self.choose_flashcards_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager
