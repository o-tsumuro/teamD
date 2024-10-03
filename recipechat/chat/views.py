from django.shortcuts import render
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import StringProperty 
from kivy.core.window import Window 
from kivy.lang import Builder
from rest_framework.decorators import api_view
from rest_framework.response import Response

# 日本語を適用させる
import japanize_kivy

# Windowの背景色を変更 (黒 → 白)
Window.clearcolor = (1, 1, 1, 1)

# class test(App):
#     def build(self):
#         title = 'GUI test'
#         return Builder.load_file('./test.kv')


# if __name__ == '__main__':
#     test().run()



@api_view(['GET'])
def get_message(request):
    return Response({"message": "Hello from Django API!"})
