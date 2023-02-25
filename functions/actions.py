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


def go_to_flashcard(_):
    Clock.schedule_once(App.get_running_app().word_page.set_focus, 0.1)
    App.get_running_app().screen_manager.current = "Flashcard"


def close_app(_):
    App.get_running_app().stop()