from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView):
    def __init__ (self,tarefas,**kwargs):#keyword arguments letra = 'a"
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text = tarefa, font_size=30))

class Test(App):
    def build(self):
        return Tarefas(['fazer comprar', 'buscar filho','molhar plantas'],orientation = 'horizontal')
    
Test( ).run( )