
__version__ = "1.0.0"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import re
import socket

class SecurityApp(App):

    def build(self):
        Window.clearcolor = (0.04, 0.07, 0.12, 1)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        self.result = Label(
            text="🛡️ أدوات الأمن السيبراني\nمرحبا بك",
            font_size=24
        )
        layout.add_widget(self.result)

        self.password = TextInput(
            hint_text="كلمة مرور تجريبية",
            multiline=False,
            password=True,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.password)

        btn1 = Button(text="معلومات الشبكة")
        btn1.bind(on_press=self.network)
        layout.add_widget(btn1)

        btn2 = Button(text="فحص كلمة المرور")
        btn2.bind(on_press=self.check_password)
        layout.add_widget(btn2)

        btn3 = Button(text="تعلم الأمن السيبراني")
        btn3.bind(on_press=self.learning)
        layout.add_widget(btn3)

        return layout

    def network(self, instance):
        try:
            ip = socket.gethostbyname(socket.gethostname())
            self.result.text = "معلومات الشبكة\nIP: " + ip
        except Exception:
            self.result.text = "تعذر الحصول على معلومات الشبكة"

    def check_password(self, instance):
        password = self.password.text
        score = 0

        score += len(password) >= 12
        score += bool(re.search(r"[A-Z]", password))
        score += bool(re.search(r"[a-z]", password))
        score += bool(re.search(r"[0-9]", password))
        score += bool(re.search(r"[^A-Za-z0-9]", password))

        if score <= 2:
            result = "كلمة المرور ضعيفة"
        elif score <= 4:
            result = "كلمة المرور متوسطة"
        else:
            result = "كلمة المرور قوية"

        self.result.text = result

    def learning(self, instance):
        self.result.text = (
            "تعلم الأمن السيبراني\n"
            "1. أساسيات Linux\n"
            "2. أساسيات الشبكات\n"
            "3. حماية الحسابات\n"
            "4. الاختراق الأخلاقي"
        )

SecurityApp().run()

