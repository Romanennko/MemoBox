from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window

from kivy.uix.screenmanager import Screen, ScreenManager


Config.set('kivy', 'window_icon', 'C:\Projects\PyCharm\MemoBox\img\icon.png')
Window.size = (1024, 768)
Window.top = 150
Window.left = 450



class StartMenu(Screen):
    pass



class MemoBoxApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(StartMenu(name='start_menu'))

        return sm



if __name__ == '__main__':
    MemoBoxApp().run()