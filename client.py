
import requests

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class MessengerApp(App):
    def build(self):
        self.layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        self.info = Label(text="Messenger")
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

        register_btn = Button(
            text="Зарегистрироваться"
        )
        register_btn.bind(on_press=self.register)
        self.layout.add_widget(register_btn)

        login_btn = Button(
            text="Войти"
        )
        login_btn.bind(on_press=self.login)
        self.layout.add_widget(login_btn)

        return self.layout


    def register(self, instance):
        data = {
            "username": self.username.text,
            "password": self.password.text
        }

        try:
            r = requests.post(
                "https://messenger-pdyf.onrender.com/register",
                json=data
            )
            self.info.text = r.json()["message"]

        except Exception as e:
            self.info.text = str(e)


    def login(self, instance):
        data = {
            "username": self.username.text,
            "password": self.password.text
        }

        try:
            r = requests.post(
                "https://messenger-pdyf.onrender.com/login",
                json=data
            )
            self.info.text = r.json()["message"]

        except Exception as e:
            self.info.text = str(e)


MessengerApp().run()
