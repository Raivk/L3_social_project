from socialnet.Graphe import Graphe,Sommet,Utilisateur,Page
import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.dictadapter import ListAdapter
from kivy.uix.listview import ListView, ListItemButton

class MainScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation="vertical"
        self.g = Graphe()
        self.to_connect = [0,0]
        self.to_disconnect = [0,0]
        self.to_destroy = 0

        add_util = Button(text="Ajouter un utilisateur")
        add_util.bind(on_press=lambda a : self.add_popup(True))

        self.add_widget(add_util)

        add_page = Button(text="Ajouter une page")
        add_page.bind(on_press=lambda a: self.add_popup(False))

        self.add_widget(add_page)

        add_connection = Button(text="Connecter")
        add_connection.bind(on_press=lambda a: self.connect_popup())

        self.add_widget(add_connection)

        del_connection = Button(text="Deconnecter")
        del_connection.bind(on_press=lambda a: self.disconnect_popup())

        self.add_widget(del_connection)

        del_som = Button(text="Supprimer un sommet")
        del_som.bind(on_press=lambda a: self.delete())

        self.add_widget(del_som)

        add_admin = Button(text="Ajouter un admin")
        add_admin.bind(on_press=lambda a: self.a_admin_popup())

        self.add_widget(add_admin)

        del_admin = Button(text="Supprimer un admin")
        del_admin.bind(on_press=lambda a: self.d_admin_popup())

        self.add_widget(del_admin)

        create_graph = Button(text="Afficher le graphe")
        create_graph.bind(on_press=lambda a : self.affiche())
        self.add_widget(create_graph)

    def a_admin(self, popup):
        self.g.get_pages()[self.to_connect[0]].add_admin(self.g.get_utils()[self.to_connect[1]])
        popup.dismiss()

    def a_admin_popup(self):
        popup = Popup(title='Ajouter un admin',
                      size_hint=(None, None), size=(400, 400), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        confirm_button = Button(text="Confirmer")
        confirm_button.disabled = True

        gl_inputs = GridLayout(cols=2)

        gl_inputs.add_widget(Label(text="Page"))
        gl_inputs.add_widget(Label(text="Utilisateur"))

        list_adapter1 = ListAdapter(data=[str(i + 1) + "- " + self.g.get_pages()[i].nom for i in range(len(self.g.get_pages()))], cls=ListItemButton,
                                        sorted_keys=[])
        list_adapter1.bind(on_selection_change=lambda a : self.selection_change(list_adapter1, 0, list_adapter2, confirm_button))
        list_view1 = ListView(adapter=list_adapter1)

        gl_inputs.add_widget(list_view1)

        list_adapter2 = ListAdapter(data=[str(i + 1) + "- " + self.g.get_utils()[i].nom for i in range(len(self.g.get_utils()))], cls=ListItemButton,
                                    sorted_keys=[])
        list_adapter2.bind(on_selection_change=lambda a : self.selection_change(list_adapter2, 1, list_adapter1, confirm_button))
        list_view2 = ListView(adapter=list_adapter2)

        gl_inputs.add_widget(list_view2)

        bl.add_widget(gl_inputs)

        confirm_button.bind(on_press=lambda a: self.a_admin(popup))
        cancel_button = Button(text="Annuler")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(confirm_button)
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()

    def d_admin(self, popup):
        popup.dismiss()
        p = self.g.get_pages()[self.to_disconnect[0]]
        p.remove_admin(p.admins[self.to_disconnect[1]])

    def d_admin_popup2(self, popup):
        popup.dismiss()

        popup = Popup(title='Choisissez un admin',
                      size_hint=(None, None), size=(400, 400), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        confirm_button = Button(text="Confirmer")
        confirm_button.disabled = True

        som = self.g.get_pages()[self.to_disconnect[0]]

        list_adapter1 = ListAdapter(
            data=[str(i + 1) + "- " + som.admins[i].nom for i in range(len(som.admins))],
            cls=ListItemButton,
            sorted_keys=[])
        list_adapter1.bind(
            on_selection_change=lambda a: self.selection_change_disco(list_adapter1, 1, confirm_button))
        list_view1 = ListView(adapter=list_adapter1)

        bl.add_widget(list_view1)

        confirm_button.bind(on_press=lambda a: self.d_admin(popup))
        cancel_button = Button(text="Annuler")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(confirm_button)
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()

    def d_admin_popup(self):
        popup = Popup(title='Choisissez une page',
                      size_hint=(None, None), size=(400, 400), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        confirm_button = Button(text="Confirmer")
        confirm_button.disabled = True

        list_adapter1 = ListAdapter(
            data=[str(i + 1) + "- " + self.g.get_pages()[i].nom for i in range(len(self.g.get_pages()))],
            cls=ListItemButton,
            sorted_keys=[])
        list_adapter1.bind(
            on_selection_change=lambda a: self.selection_change_disco(list_adapter1, 0, confirm_button))
        list_view1 = ListView(adapter=list_adapter1)

        bl.add_widget(list_view1)

        confirm_button.bind(on_press=lambda a: self.d_admin_popup2(popup))
        cancel_button = Button(text="Annuler")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(confirm_button)
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()


    def selection_change_del(self,adapter, confirmButton):
        self.to_destroy = int(adapter.selection[0].text[0]) - 1
        confirmButton.disabled = False

    def delete(self):
        popup = Popup(title='Choisissez un sommet a supprimer',
                      size_hint=(None, None), size=(400, 400), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        confirm_button = Button(text="Confirmer")
        confirm_button.disabled = True

        list_adapter1 = ListAdapter(
            data=[str(i + 1) + "- " + self.g.get_sommets()[i].nom for i in range(len(self.g.get_sommets()))],
            cls=ListItemButton,
            sorted_keys=[])
        list_adapter1.bind(
            on_selection_change=lambda a: self.selection_change_del(list_adapter1, confirm_button))
        list_view1 = ListView(adapter=list_adapter1)

        bl.add_widget(list_view1)

        confirm_button.bind(on_press=lambda a: self.delete_confirm(popup))
        cancel_button = Button(text="Annuler")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(confirm_button)
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()

    def delete_confirm(self, popup):
        self.g.remove_sommet(self.g.get_sommets()[self.to_destroy])
        popup.dismiss()

    def connect(self,popup):
        self.g.connect(self.g.get_sommets()[self.to_connect[0]],
                       self.g.get_sommets()[self.to_connect[1]])
        popup.dismiss()

    def selection_change(self, adapter, pos, adapter2, confirmButton):
        if len(adapter.selection) == 1 and len(adapter2.selection) == 1:
            confirmButton.disabled = False
        self.to_connect[pos] = int(adapter.selection[0].text[0]) - 1

    def selection_change_disco(self, adapter, pos, confirmButton):
        self.to_disconnect[pos] = int(adapter.selection[0].text[0]) - 1
        confirmButton.disabled = False

    def disconnect(self, som, popup):
        popup.dismiss()
        self.g.disconnect(som, som.out[self.to_disconnect[1]])

    def disconnect_popup2(self, popup):
        popup.dismiss()

        popup = Popup(title='Choisissez un second sommet',
                      size_hint=(None, None), size=(400, 400), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        confirm_button = Button(text="Confirmer")
        confirm_button.disabled = True

        som = self.g.get_sommets()[self.to_disconnect[0]]

        list_adapter1 = ListAdapter(
            data=[str(i + 1) + "- " + som.out[i].nom for i in range(len(som.out))],
            cls=ListItemButton,
            sorted_keys=[])
        list_adapter1.bind(
            on_selection_change=lambda a: self.selection_change_disco(list_adapter1, 1, confirm_button))
        list_view1 = ListView(adapter=list_adapter1)

        bl.add_widget(list_view1)

        confirm_button.bind(on_press=lambda a: self.disconnect(som, popup))
        cancel_button = Button(text="Annuler")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(confirm_button)
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()

    def disconnect_popup(self):
        popup = Popup(title='Choisissez un premier sommet',
                      size_hint=(None, None), size=(400, 400), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        confirm_button = Button(text="Confirmer")
        confirm_button.disabled = True

        list_adapter1 = ListAdapter(
            data=[str(i + 1) + "- " + self.g.get_sommets()[i].nom for i in range(len(self.g.get_sommets()))],
            cls=ListItemButton,
            sorted_keys=[])
        list_adapter1.bind(
            on_selection_change=lambda a: self.selection_change_disco(list_adapter1, 0, confirm_button))
        list_view1 = ListView(adapter=list_adapter1)

        bl.add_widget(list_view1)

        confirm_button.bind(on_press=lambda a: self.disconnect_popup2(popup))
        cancel_button = Button(text="Annuler")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(confirm_button)
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()

    def connect_popup(self):
        popup = Popup(title='Connecter deux sommets',
                      size_hint=(None, None), size=(400, 400), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        confirm_button = Button(text="Confirmer")
        confirm_button.disabled = True

        gl_inputs = GridLayout(cols=2)

        gl_inputs.add_widget(Label(text="Sommet 1"))
        gl_inputs.add_widget(Label(text="Sommet 2"))

        list_adapter1 = ListAdapter(data=[str(i + 1) + "- " + self.g.get_sommets()[i].nom for i in range(len(self.g.get_sommets()))], cls=ListItemButton,
                                        sorted_keys=[])
        list_adapter1.bind(on_selection_change=lambda a : self.selection_change(list_adapter1, 0, list_adapter2, confirm_button))
        list_view1 = ListView(adapter=list_adapter1)

        gl_inputs.add_widget(list_view1)

        list_adapter2 = ListAdapter(data=[str(i + 1) + "- " + self.g.get_sommets()[i].nom for i in range(len(self.g.get_sommets()))], cls=ListItemButton,
                                    sorted_keys=[])
        list_adapter2.bind(on_selection_change=lambda a : self.selection_change(list_adapter2, 1, list_adapter1, confirm_button))
        list_view2 = ListView(adapter=list_adapter2)

        gl_inputs.add_widget(list_view2)

        bl.add_widget(gl_inputs)

        confirm_button.bind(on_press=lambda a: self.connect(popup))
        cancel_button = Button(text="Annuler")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(confirm_button)
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()

    def add_popup(self,isUtil):
        if isUtil:
            popup = Popup(title='Ajouter un Utilisateur',
                          size_hint=(None, None), size=(400, 400), auto_dismiss=False)
            bl = BoxLayout(orientation='vertical')

            gl_inputs = GridLayout(cols=2)
            gl_inputs.som_name = TextInput(multiline=False)
            gl_inputs.add_widget(Label(text="Nom de l'utilisateur : "))
            gl_inputs.add_widget(gl_inputs.som_name)
            gl_inputs.add_widget(Label(text="Prenom de l'utilisateur"))
            gl_inputs.som_firstname = TextInput(multiline=False)
            gl_inputs.add_widget(gl_inputs.som_firstname)
            gl_inputs.add_widget(Label(text="Age de l'utilisateur"))
            gl_inputs.som_age = TextInput(multiline=False, input_filter='int')
            gl_inputs.add_widget(gl_inputs.som_age)

            bl.add_widget(gl_inputs)

            confirm_button = Button(text="Confirmer")
            confirm_button.bind(on_press=lambda a: self.add_sommet_popup(popup,"Utilisateur",gl_inputs.som_name.text,gl_inputs.som_firstname.text,gl_inputs.som_age.text))
            cancel_button = Button(text="Annuler")
            cancel_button.bind(on_press=lambda a: popup.dismiss())
            bl.add_widget(confirm_button)
            bl.add_widget(cancel_button)
            popup.content = bl
            popup.open()
        else:
            popup = Popup(title='Ajouter une Page',
                          size_hint=(None, None), size=(400, 400), auto_dismiss=False)
            bl = BoxLayout(orientation='vertical')

            gl_inputs = GridLayout(cols=2)
            gl_inputs.som_name = TextInput(multiline=False)
            gl_inputs.add_widget(Label(text="Nom de la page : "))
            gl_inputs.add_widget(gl_inputs.som_name)

            bl.add_widget(gl_inputs)

            confirm_button = Button(text="Confirmer")
            confirm_button.bind(on_press=lambda a : self.add_sommet_popup(popup,"Page",gl_inputs.som_name.text))
            cancel_button = Button(text="Annuler")
            cancel_button.bind(on_press=lambda a : popup.dismiss())
            bl.add_widget(confirm_button)
            bl.add_widget(cancel_button)
            popup.content = bl
            popup.open()

    def add_sommet_popup(self, popup, type, name, firstname="default", age=0):
        if type == "Utilisateur":
            self.g.add_sommet(Utilisateur(name, firstname, age))
            popup.dismiss()
        if type == "Page":
            self.g.add_sommet(Page(name))
            popup.dismiss()

    def affiche(self):
        self.g.affiche()

class TestApp(App):
    def build(self):
        return MainScreen()

TestApp().run()
