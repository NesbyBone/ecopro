#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager,Screen

from Scripts.padnumerico import Pad
from Media.Textos import Textos

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')

class ECO(ScreenManager):
    pass

class Inicio(Screen):
    TInstrucciones = Textos.instrucciones

class PadNumerico(Screen):
    pass

class Informacion(Screen):
    pass

class MainApp(App):
    title = "ECO App"
    def build(self):
        return ECO()

if __name__ == '__main__':
    MainApp().run()