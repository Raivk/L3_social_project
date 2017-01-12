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
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.filechooser import FileChooserIconView

class MainScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation="vertical"
        self.g = Graphe()
        self.to_connect = [0,0]
        self.to_disconnect = [0,0]
        self.to_destroy = 0

        gest_sommet = Button(text="Gestion des sommets")
        gest_sommet.bind(on_press=lambda a : self.gest_s())

        self.add_widget(gest_sommet)

        gest_arcs = Button(text="Gestion des arcs")
        gest_arcs.bind(on_press=lambda a : self.gest_ar())

        self.add_widget(gest_arcs)

        gest_ads = Button(text="Gestion des admins")
        gest_ads.bind(on_press=lambda a : self.gest_ad())

        self.add_widget(gest_ads)

        display_soms = Button(text="Parcourir les sommets")
        display_soms.bind(on_press=lambda a: self.parcours())

        self.add_widget(display_soms)

        algos = Button(text="Algos")
        algos.bind(on_press=lambda a:self.algos())

        self.add_widget(algos)

        loadsave = Button(text="Charger/Sauvegarder")
        loadsave.bind(on_press=lambda a: self.popup_loadsave())

        self.add_widget(loadsave)

        create_graph = Button(text="Afficher le graphe")
        create_graph.bind(on_press=lambda a : self.affiche())
        self.add_widget(create_graph)

        list_succ = Button(text="Afficher par liste de successeurs")
        list_succ.bind(on_press=lambda a : self.aff_list_succ())
        self.add_widget(list_succ)

        stats = Button(text="Statistiques")
        stats.bind(on_press=lambda a : self.statist())
        self.add_widget(stats)

    def statist(self):
        popup = Popup(title='Liste de successeurs', size_hint=(0.9, 0.9), auto_dismiss=False)
        bl = BoxLayout(orientation="vertical")

        res = ""

        res += "Moyenne d'age : " + str(self.g.get_moy_age()) + "\n"
        res += "Nombre de pages : " + str(self.g.get_nb_page()) + "\n"
        res += "Nombre d'utilisateurs : " + str(self.g.get_nb_util()) + "\n"
        res += "Nombre de sommets : " + str(self.g.som_len()) + "\n"
        res += "Nombre d'arcs : " + str(self.g.arc_len())

        bl.add_widget(Label(text=res))

        bt = Button(text="Fermer")
        bt.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(bt)
        popup.content = bl
        popup.open()

    def aff_list_succ(self):
        popup = Popup(title='Liste de successeurs', size_hint=(0.9, 0.9), auto_dismiss=False)
        bl = BoxLayout(orientation="vertical")

        list_adapter1 = ListAdapter(
            data=[str(i + 1) + "- " + self.g.get_sommets()[i].__repr__() for i in range(len(self.g.get_sommets()))],
            cls=ListItemButton,
            sorted_keys=[])
        list_adapter1.bind(on_selection_change=lambda a: self.selected(list_adapter1,"no_filter"))
        list_view1 = ListView(adapter=list_adapter1)

        bl.add_widget(list_view1)

        bt = Button(text="Fermer")
        bt.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(bt)
        popup.content = bl
        popup.open()

    def gest_ar(self):
        popup = Popup(title='Gestion des arcs',
                     size_hint=(0.9, 0.9), auto_dismiss=False)
        bl = BoxLayout(orientation="vertical")

        add_connection = Button(text="Connecter")
        add_connection.bind(on_press=lambda a: self.connect_popup())
        add_connection.bind(on_release=lambda a: popup.dismiss())

        bl.add_widget(add_connection)

        del_connection = Button(text="Deconnecter")
        del_connection.bind(on_press=lambda a: self.disconnect_popup())
        del_connection.bind(on_release=lambda a: popup.dismiss())

        bl.add_widget(del_connection)

        bt = Button(text="Fermer")
        bt.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(bt)
        popup.content = bl
        popup.open()

    def gest_ad(self):
        popup = Popup(title='Gestion des admins',
                     size_hint=(0.9, 0.9), auto_dismiss=False)
        bl = BoxLayout(orientation="vertical")

        add_admin = Button(text="Ajouter un admin")
        add_admin.bind(on_press=lambda a: self.a_admin_popup())
        add_admin.bind(on_release=lambda a: popup.dismiss())

        bl.add_widget(add_admin)

        del_admin = Button(text="Supprimer un admin")
        del_admin.bind(on_press=lambda a: self.d_admin_popup())
        del_admin.bind(on_release=lambda a: popup.dismiss())

        bl.add_widget(del_admin)

        bt = Button(text="Fermer")
        bt.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(bt)
        popup.content = bl
        popup.open()

    def gest_s(self):
        popup = Popup(title='Gestion des sommets',
                     size_hint=(0.9, 0.9), auto_dismiss=False)
        bl = BoxLayout(orientation="vertical")

        add_util = Button(text="Ajouter un utilisateur")
        add_util.bind(on_press=lambda a: self.add_popup(True))
        add_util.bind(on_release=lambda a: popup.dismiss())

        bl.add_widget(add_util)

        add_page = Button(text="Ajouter une page")
        add_page.bind(on_press=lambda a: self.add_popup(False))
        add_page.bind(on_release=lambda a: popup.dismiss())

        bl.add_widget(add_page)

        del_som = Button(text="Supprimer un sommet")
        del_som.bind(on_press=lambda a: self.delete())
        del_som.bind(on_release=lambda a: popup.dismiss())

        bl.add_widget(del_som)

        bt = Button(text="Fermer")
        bt.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(bt)
        popup.content = bl
        popup.open()

    def load_confirm(self, selection, popup):
        if len(selection) > 0:
            self.g.ouv(selection[0])
            popup.dismiss()
        else:
            pop = Popup(title='Pas de fichier selectionne',
                   size_hint=(0.9, 0.9), auto_dismiss=False)
            bl = BoxLayout()
            bt = Button(text="Fermer")
            bt.bind(on_press=lambda a : pop.dismiss())
            bl.add_widget(bt)
            pop.content = bl
            pop.open()

    def load(self, popup):
        popup.dismiss()

        popup = Popup(title='Charger',
                       size_hint=(0.9, 0.9), auto_dismiss=False)
        bl_main = BoxLayout(orientation='vertical')
        bl = BoxLayout(orientation='vertical')

        flc = FileChooserIconView()

        bl_main.add_widget(flc)

        confirm_button = Button(text="Confirmer")
        confirm_button.bind(on_press=lambda a: self.load_confirm(flc.selection, popup))
        bl.add_widget(confirm_button)

        cancel_button = Button(text="Annuler")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(cancel_button)

        bl_main.add_widget(bl)

        popup.content = bl_main
        popup.open()


    def p_newfile_confirm(self,popup,text):
        print(text)
        open(text, 'a').close()
        popup.dismiss()

    def p_newfile(self,path):
        pop = Popup(title='Nouveau fichier',
                     size_hint=(0.9, 0.9), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        text = TextInput()
        bl.add_widget(text)

        btc = Button(text="Confirmer")
        btc.bind(on_press=lambda a: self.p_newfile_confirm(pop, path + "/" + text.text + ".projpy"))
        bl.add_widget(btc)

        btf = Button(text="Fermer")
        btf.bind(on_press=lambda a: pop.dismiss())
        bl.add_widget(btf)
        pop.content = bl
        pop.open()

    def save_confirm(self, selection, popup):
        if len(selection) > 0:
            self.g.save(selection[0])
            popup.dismiss()
        else:
            pop = Popup(title='Pas de fichier selectionne',
                         size_hint=(0.9, 0.9), auto_dismiss=False)
            bl = BoxLayout()
            bt = Button(text="Fermer")
            bt.bind(on_press=lambda a: pop.dismiss())
            bl.add_widget(bt)
            pop.content = bl
            pop.open()

    def save(self, popup):
        popup.dismiss()

        popup = Popup(title='Charger',
                       size_hint=(0.9, 0.9), auto_dismiss=False)
        bl_main = BoxLayout(orientation='vertical')
        bl = BoxLayout(orientation='vertical')

        flc = FileChooserIconView()

        bl_main.add_widget(flc)

        newFile = Button(text="Nouveau fichier")
        newFile.bind(on_press=lambda a : self.p_newfile(flc.path))
        bl.add_widget(newFile)

        confirm = Button(text="Confirmer")
        confirm.bind(on_press=lambda a : self.save_confirm(flc.selection,popup))
        bl.add_widget(confirm)

        cancel_button = Button(text="Annuler")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(cancel_button)

        bl_main.add_widget(bl)

        popup.content = bl_main
        popup.open()

    def popup_loadsave(self):
        popup = Popup(title='Charger / Sauvegarder',
                       size_hint=(0.9, 0.9), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        load = Button(text="Charger")
        load.bind(on_press=lambda a: self.load(popup))

        bl.add_widget(load)

        save = Button(text="Sauvegarder")
        save.bind(on_press=lambda a: self.save(popup))

        bl.add_widget(save)

        cancel_button = Button(text="Annuler")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()


    def popup_pagerank(self,popup):
        popup.dismiss()

        popup = Popup(title='PageRank',
                       size_hint=(0.9, 0.9), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        pr = self.g.page_rank()

        list_adapter1 = ListAdapter(
            data=[keySom.nom + " : " + str(pr[keySom]) for keySom in pr.keys()],
            cls=ListItemButton,
            sorted_keys=[])
        list_view1 = ListView(adapter=list_adapter1)

        bl.add_widget(list_view1)

        cancel_button = Button(text="Annuler")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()

    def disp_pcd(self,som):
        popup = Popup(title='Plus courtes distances',
                       size_hint=(0.9, 0.9), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        pcd = self.g.plus_courte_distance(som)

        list_adapter1 = ListAdapter(
            data=[keySom.nom + " : " + str(pcd[keySom]) for keySom in pcd.keys()],
            cls=ListItemButton,
            sorted_keys=[])
        list_view1 = ListView(adapter=list_adapter1)

        bl.add_widget(list_view1)

        cancel_button = Button(text="Annuler")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()

    def pcd_change(self,adapter):
        if len(adapter.selection) > 0:
            res = ""
            for i in range(0, len(adapter.selection[0].text)):
                if adapter.selection[0].text[i] == "-":
                    res = adapter.selection[0].text[0: i]
            self.disp_pcd(self.g.get_sommets()[int(res) - 1])

    def popup_pcd(self,popup):
        popup.dismiss()

        popup = Popup(title='Choisissez un sommet',
                       size_hint=(0.9, 0.9), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        list_adapter1 = ListAdapter(
            data=[str(i + 1) + "- " + self.g.get_sommets()[i].nom for i in range(len(self.g.get_sommets()))],
            cls=ListItemButton,
            sorted_keys=[])
        list_adapter1.bind(on_selection_change=lambda a: self.pcd_change(list_adapter1))
        list_view1 = ListView(adapter=list_adapter1)

        bl.add_widget(list_view1)

        cancel_button = Button(text="Annuler")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()

    def algos(self):
        popup = Popup(title='Executer un algorithme',
                       size_hint=(0.9, 0.9), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        pr = Button(text="PageRank")
        pr.bind(on_press=lambda a: self.popup_pagerank(popup))

        pcd = Button(text="Plus courtes distances")
        pcd.bind(on_press=lambda a: self.popup_pcd(popup))

        bl.add_widget(pr)
        bl.add_widget(pcd)

        cancel_button = Button(text="Annuler")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()

    def p_name(self,popup):
        popup.dismiss()

        popup = Popup(title='Sommets par nom',
                       size_hint=(0.9, 0.9), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        list_adapter1 = ListAdapter(
            data=[str(i + 1) + "- " + self.g.get_sommets_by_name()[i].nom for i in range(len(self.g.get_sommets()))],
            cls=ListItemButton,
            sorted_keys=[])
        list_adapter1.bind(on_selection_change=lambda a : self.selected(list_adapter1,"name"))
        list_view1 = ListView(adapter=list_adapter1)

        bl.add_widget(list_view1)

        cancel_button = Button(text="Fermer")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()

    def selected(self, adapter, filter):
        if len(adapter.selection) > 0:
            res = 0
            for i in range(0, len(adapter.selection[0].text)):
                if adapter.selection[0].text[i] == "-":
                    res = adapter.selection[0].text[0:i]
            pos = int(res) - 1
            if filter == "name":
                self.p_display(self.g.get_sommets_by_name()[pos])
            if filter == "degre":
                self.p_display(self.g.get_sommets_by_degree()[pos])
            if filter == "no_filter":
                self.p_display(self.g.get_sommets()[pos])

    def p_degree(self,popup):
        popup.dismiss()

        popup = Popup(title='Sommets par degre',
                       size_hint=(0.9, 0.9), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        list_adapter1 = ListAdapter(
            data=[str(i + 1) + "- " + self.g.get_sommets_by_degree()[i].nom for i in range(len(self.g.get_sommets()))],
            cls=ListItemButton,
            sorted_keys=[])
        list_adapter1.bind(on_selection_change=lambda a : self.selected(list_adapter1,"degre"))
        list_view1 = ListView(adapter=list_adapter1)

        bl.add_widget(list_view1)

        cancel_button = Button(text="Fermer")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()

    def p_find(self,popup):
        popup.dismiss()

        popup = Popup(title='Chercher un sommet',
                       size_hint=(0.9, 0.9), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        confirmButton = Button(text="Confirmer")

        som_name = TextInput(multiline=False)

        confirmButton.bind(on_press= lambda a : self.p_display(self.g.find_name(som_name.text)))

        bl.add_widget(som_name)

        bl.add_widget(confirmButton)

        cancel_button = Button(text="Fermer")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()

    def p_display(self, som):
        bl = BoxLayout(orientation='vertical')

        if isinstance(som, Page):
            popup = Popup(title='Page :',
                           size_hint=(0.9, 0.9), auto_dismiss=False)
            l = Label(text=som.__repr__())
            bl.add_widget(l)
        else:
            if isinstance(som, Utilisateur):
                popup = Popup(title='Utilisateur :',
                             size_hint=(0.9, 0.9), auto_dismiss=False)
                l = Label(text=som.__repr__())
                bl.add_widget(l)
            else:
                popup = Popup(title='Impossible de trouver le sommet !')

        cancel_button = Button(text="Fermer")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()

    def parcours(self):
        popup = Popup(title='Ajouter un admin',
                       size_hint=(0.9, 0.9), auto_dismiss=False)
        bl = BoxLayout(orientation='vertical')

        by_name = Button(text="Par nom")
        by_name.bind(on_press=lambda  a: self.p_name(popup))

        by_degree = Button(text="Par degre")
        by_degree.bind(on_press=lambda a: self.p_degree(popup))

        search = Button(text="Rechercher...")
        search.bind(on_press=lambda a: self.p_find(popup))

        bl.add_widget(by_name)
        bl.add_widget(by_degree)
        bl.add_widget(search)

        cancel_button = Button(text="Annuler")
        cancel_button.bind(on_press=lambda a: popup.dismiss())
        bl.add_widget(cancel_button)

        popup.content = bl
        popup.open()

    def a_admin(self, popup):
        self.g.get_pages()[self.to_connect[0]].add_admin(self.g.get_utils()[self.to_connect[1]])
        popup.dismiss()

    def a_admin_popup(self):
        popup = Popup(title='Ajouter un admin',
                       size_hint=(0.9, 0.9), auto_dismiss=False)
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
                       size_hint=(0.9, 0.9), auto_dismiss=False)
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
                       size_hint=(0.9, 0.9), auto_dismiss=False)
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
        if len(adapter.selection) > 0:
            res = ""
            for i in range(0, len(adapter.selection[0].text)):
                if adapter.selection[0].text[i] == "-":
                    res = adapter.selection[0].text[0: i]
            self.to_destroy = int(res) - 1
            confirmButton.disabled = False
        else:
            confirmButton.disabled = True

    def delete(self):
        popup = Popup(title='Choisissez un sommet a supprimer',
                       size_hint=(0.9, 0.9), auto_dismiss=False)
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
        if len(adapter.selection) > 0:
            res = ""
            for i in range(0, len(adapter.selection[0].text)):
                if adapter.selection[0].text[i] == "-":
                    res = adapter.selection[0].text[0: i]
            self.to_connect[pos] = int(res) - 1
        else:
            confirmButton.disabled = True

    def selection_change_disco(self, adapter, pos, confirmButton):
        if len(adapter.selection) > 0:
            res = ""
            for i in range(0,len(adapter.selection[0].text)):
                if adapter.selection[0].text[i] == "-":
                    res = adapter.selection[0].text[0 : i]
            self.to_disconnect[pos] = int(res) - 1
            confirmButton.disabled = False
        else:
            confirmButton.disabled = True

    def disconnect(self, som, popup):
        popup.dismiss()
        self.g.disconnect(som, som.out[self.to_disconnect[1]])

    def disconnect_popup2(self, popup):
        popup.dismiss()

        popup = Popup(title='Choisissez un second sommet',
                       size_hint=(0.9, 0.9), auto_dismiss=False)
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
                       size_hint=(0.9, 0.9), auto_dismiss=False)
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
                       size_hint=(0.9, 0.9), auto_dismiss=False)
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
                           size_hint=(0.9, 0.9), auto_dismiss=False)
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
                           size_hint=(0.9, 0.9), auto_dismiss=False)
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
            if len(age) == 0:
                age = 0
            else:
                age = int(age)
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
