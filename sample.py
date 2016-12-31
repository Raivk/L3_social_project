from socialnet.Graphe import Graphe,Sommet,Utilisateur,Page
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown


class MainScreen(GridLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2

        g = Graphe()

        gl_inputs = GridLayout(cols=2)
        gl_inputs.som_name = TextInput(multiline = False)
        gl_inputs.add_widget(Label(text="Nom du sommet : "))
        gl_inputs.add_widget(gl_inputs.som_name)
        gl_inputs.add_widget(Label(text="Prenom de l'utilisateur"))
        gl_inputs.som_firstname = TextInput(multiline = False)
        gl_inputs.add_widget(gl_inputs.som_firstname)
        gl_inputs.add_widget(Label(text="Age de l'utilisateur"))
        gl_inputs.som_age = TextInput(multiline = False, input_filter='int')
        gl_inputs.add_widget(gl_inputs.som_age)
        gl_inputs.add_widget(Label(text="selectionnez un type : "))

        dropdown = DropDown()
        btn = Button(text='Utilisateur', size_hint_y=None, height=44)
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)
        btn2 = Button(text='Page', size_hint_y=None, height=44)
        btn2.bind(on_release=lambda btn2: dropdown.select(btn2.text))
        dropdown.add_widget(btn2)
        mainbutton = Button(text='Utilisateur', size_hint=(None, None))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        gl_inputs.add_widget(mainbutton)

        add_sommet = Button(text="Ajouter un sommet")
        add_sommet.bind(on_press=lambda a : self.add_sommet(g, mainbutton.text, gl_inputs.som_name.text, gl_inputs.som_firstname.text, gl_inputs.som_age.text))

        self.add_widget(add_sommet)
        self.add_widget(gl_inputs)

        create_graph = Button(text="Afficher le graphe")
        create_graph.bind(on_press=lambda a : self.callback(g))
        self.add_widget(create_graph)

    def add_sommet(self, g, type, name, firstname="default", age=0):
        if type == "Utilisateur":
            g.add_sommet(Utilisateur(name, firstname, age))
        if type == "Page":
            g.add_sommet(Page(name))

    def callback(self, g):
        print(g)

class TestApp(App):
    def build(self):
        return MainScreen()

TestApp().run()
