from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivymd.uix.behaviors.hover_behavior import HoverBehavior

from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.uix.button import Button

Config.set('kivy', 'window_icon', 'C:\Projects\PyCharm\MemoBox\img\icon.png')
Window.size = (1024, 768)
Window.top = 150
Window.left = 450



class StyledButton(Button, HoverBehavior):
    background = ListProperty((1, 1, 1, 0))

    def on_enter(self):
        self.background = (255, 255, 255, 0.1)

    def on_leave(self):
        self.background = (255, 255, 255, 0)



class StartMenu(Screen):
    pass


class ProfileMenu(Screen):
    pass



class WatchMenu(Screen):
    pass



class TaskMenu(Screen):
    pass



class SavedMenu(Screen):
    pass



class MemoBoxApp(App, Screen):
    def build(self):
        self.sm = ScreenManager()

        self.sm.add_widget(StartMenu(name='start_menu'))
        self.sm.add_widget(ProfileMenu(name='profile_menu'))
        self.sm.add_widget(WatchMenu(name='watch_menu'))
        self.sm.add_widget(TaskMenu(name='task_menu'))
        self.sm.add_widget(SavedMenu(name='saved_menu'))

        return self.sm

    def toggle_menu(self):
        menu = self.sm.get_screen('start_menu').ids.sidebar
        if menu.opacity == 0:
            menu.opacity = 1
        else:
            menu.opacity = 0



if __name__ == '__main__':
    MemoBoxApp().run()