from kivy.app import App
from kivy.clock import Clock


def go_to_menu(_):
    App.get_running_app().screen_manager.current = "EntryPage"


def go_to_add_word_page(_):
    App.get_running_app().screen_manager.current = "AddWord"


def go_to_create_new_list_page(_):
    App.get_running_app().screen_manager.current = "CreateNewList"


def go_to_setting_page(_):
    App.get_running_app().screen_manager.current = "Settings"


def go_to_add_choose_page(_):
    App.get_running_app().screen_manager.current = "AddChoosePage"


def go_to_flashcard(flashcard_list):
    Clock.schedule_once(App.get_running_app().word_page.set_focus, 0.1)
    App.get_running_app().screen_manager.current = "Flashcard"
    mode = App.get_running_app().choose_flashcards_page.checkbox_mode()
    App.get_running_app().word_page.set_mode(mode)
    App.get_running_app().word_page.open_flashcard_page(flashcard_list)


def go_to_choose_flashcards_page(_):
    App.get_running_app().screen_manager.current = "ChooseFlashcards"


def close_app(_):
    App.get_running_app().stop()
