# -*- coding: utf-8 -*-
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

class Pad(BoxLayout):
    None

class Numerico(GridLayout):
    contenedor = ObjectProperty(None)
    def set_numero(self, n):
        display = self.contenedor.ids.Display
        if len(display.text) < 8:
            display.text = display.text + n

    def borrar(self):
        display = self.contenedor.ids.Display
        t = display.text
        display.text = t[0:len(t)-1]
