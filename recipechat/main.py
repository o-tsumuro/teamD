import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import requests

class MyLayout(BoxLayout):
    def get_data_from_api(self):
        try:
            # Django APIにリクエストを送信
            response = requests.get('http://127.0.0.1:8000/')
            if response.status_code == 200:
                # レスポンスのデータを取得し、ラベルに表示
                data = response.json()
                self.ids.label.text = data['message']
            else:
                self.ids.label.text = "Failed to get data"
        except Exception as e:
            self.ids.label.text = f"Error: {e}"

class MyApp(App):
    def build(self):
        layout = MyLayout()
        return layout

if __name__ == '__main__':
    MyApp().run()
