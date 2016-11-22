from socialnet.Graphe import Graphe,Sommet,Utilisateur,Page
import time

g = Graphe()
gtest = Graphe()
u = Utilisateur("Perroni","Pep",50)
u2 = Utilisateur("test","nucleaire",20)
p = Page("DogeLand.com")

g.add_sommet(u)
g.add_sommet(p)
u.connect(p)
u.connect(u2)
u2.connect(u)

print(g)
print(u)
print(p)
print(g.som_len())
print(g.arc_len())
print(g.get_sommets_by_name())
print(g.get_sommets_by_degree())
print(g.get_arcs())
print("------------")

g.add_sommet(u2)
p.add_admin(u2)
print(g.get_nb_util())
print(g.get_nb_page())
print(g.get_moy_age())
print(g.get_admins())
g.save()
gtest.ouv("lasauvegardedelamortquitue.stylux")

print("test save charge")

print(gtest.som_len())
print(g.som_len())
print(gtest.arc_len())
print(g.arc_len())
print(gtest.get_sommets_by_name())
print(g.get_sommets_by_name())
print(gtest.get_sommets_by_degree())
print(g.get_sommets_by_degree())
print(gtest.get_arcs())
print(g.get_arcs())
print("------------")
print(gtest.get_nb_util())
print(g.get_nb_util())
print(gtest.get_nb_page())
print(g.get_nb_page())
print(gtest.get_moy_age())
print(g.get_moy_age())
print(gtest.get_admins())
print(g.get_admins())



# from kivy.app import App
# from kivy.uix.button import Button
#
#
# class TestApp(App):
#     def build(self):
#         return Button(text='Hello World')
#
# TestApp().run()
