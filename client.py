import requests

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class MessengerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.info = Label(text="Регистрация")
        self.layout.add_widget(self.info)

        self.username = TextInput(
            hint_text="Логин",
            multiline=False
        )
        self.layout.add_widget(self.username)

        self.password = TextInput(
            hint_text="Пароль",
            password=True,
            multiline=False
        )
        self.layout.add_widget(self.password)

        btn = Button(
            text="Зарегистрироваться"
        )
        btn.bind(on_press=self.register)
        self.layout.add_widget(btn)

        return self.layout

    def register(self, instance):
        data = {
            "username": self.username.text,
            "password": self.password.text
        }

        try:
            r = requests.post(
                "http://127.0.0.1:8000/register",
                json=data
            )
            self.info.text = r.json()["message"]
        except Exception:
            self.info.text = "Сервер недоступен!"


MessengerApp().run()