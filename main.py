from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivymd.uix.behaviors.hover_behavior import HoverBehavior

Config.set("kivy", "window_icon", r"C:\Projects\PyCharm\MemoBox\img\icon.png")
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
    def add_task_popup(self):
        content = BoxLayout(orientation="vertical")

        # Name task
        content.add_widget(Label(text="Enter a name task"))
        task_name = TextInput(hint_text="drink one million beer", multiline=False)
        content.add_widget(task_name)

        # description task
        content.add_widget(Label(text="Add description for the task"))
        task_description = TextInput(hint_text="This is sigma task!!!")
        content.add_widget(task_description)

        # Status task
        content.add_widget(Label(text="Select a status for the task"))

        self.task_dropdown_status = DropDown()

        for option in ["Not started", "In progress", "Done"]:
            btn = Button(text=option, size_hint_y=None, height=44)

            btn.bind(
                on_press=lambda btn: self.select_option(
                    "task_dropdown_status", btn.text
                )
            )

            self.task_dropdown_status.add_widget(btn)

        self.task_status_button = Button(text="Select status")

        self.task_status_button.bind(on_release=self.task_dropdown_status.open)
        content.add_widget(self.task_status_button)

        # Priority task
        content.add_widget(Label(text="Select priority for your task"))

        self.task_dropdown_priority = DropDown()

        for option in ["A", "B", "C", "D"]:
            btn = Button(text=option, size_hint_y=None, height=44)

            btn.bind(
                on_press=lambda btn: self.select_option(
                    "task_dropdown_priority", btn.text
                )
            )

            self.task_dropdown_priority.add_widget(btn)

        self.task_priority_button = Button(text="Select priority")
        self.task_priority_button.bind(on_release=self.task_dropdown_priority.open)
        content.add_widget(self.task_priority_button)

        # Deadline task
        content.add_widget(Label(text="Enter deadline for this task"))
        task_deadline = TextInput(hint_text="22.01.2007, 9:00 or 22.01.2007 or 9:00")
        content.add_widget(task_deadline)

        # Tags task
        content.add_widget(Label(text="Select tag for task"))

        self.task_dropdown_tag = DropDown()

        for option in ["Life", "University"]:
            btn = Button(text=option, size_hint_y=None, height=44)

            btn.bind(
                on_press=lambda btn: self.select_option("task_dropdown_tag", btn.text)
            )

            self.task_dropdown_tag.add_widget(btn)

        self.task_tag_button = Button(text="Select tag")
        self.task_tag_button.bind(on_release=self.task_dropdown_tag.open)
        content.add_widget(self.task_tag_button)

        content_button = BoxLayout(orientation="horizontal")

        back_button = Button(text="Back")
        back_button.bind(on_press=self.close_popup)
        content_button.add_widget(back_button)

        add_task_button = Button(text="Add task")
        add_task_button.bind(on_press=self.close_popup)
        content_button.add_widget(add_task_button)

        content.add_widget(content_button)

        # Popup for add task
        self.add_task_popup_screen = Popup(
            title="Add task",
            content=content,
            size_hint=(0.95, 0.95),
            auto_dismiss=False,
        )

        self.add_task_popup_screen.open()

    def select_option(self, dropdown, option_text):
        if dropdown == "task_dropdown_status":
            self.task_dropdown_status.dismiss()
            self.task_status_button.text = option_text
        elif dropdown == "task_dropdown_priority":
            self.task_dropdown_priority.dismiss()
            self.task_priority_button.text = option_text
        elif dropdown == "task_dropdown_tag":
            self.task_dropdown_tag.dismiss()
            self.task_tag_button.text = option_text

    def close_popup(self, instance):
        self.add_task_popup_screen.dismiss()


class SavedMenu(Screen):
    pass


class MemoBoxApp(App, Screen):
    def build(self):
        self.sm = ScreenManager()

        self.sm.add_widget(StartMenu(name="start_menu"))
        self.sm.add_widget(ProfileMenu(name="profile_menu"))
        self.sm.add_widget(WatchMenu(name="watch_menu"))
        self.sm.add_widget(TaskMenu(name="task_menu"))
        self.sm.add_widget(SavedMenu(name="saved_menu"))

        return self.sm

    def toggle_menu(self, screen_name):
        menu = self.sm.get_screen(screen_name).ids.sidebar
        if menu.opacity == 0:
            menu.opacity = 1
        else:
            menu.opacity = 0


if __name__ == "__main__":
    MemoBoxApp().run()
