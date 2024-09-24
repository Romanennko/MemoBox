from kivy.app import App

from kivy.uix.screenmanager import Screen, ScreenManager


class StartMenu(Screen):
    pass



class MemoBoxApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(StartMenu(name='start_menu'))

        return sm



if __name__ == '__main__':
    MemoBoxApp().run()