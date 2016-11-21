from socialnet.Graphe import Graphe,Sommet,Utilisateur,Page

g = Graphe()
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
g.ouv("lasauvegardedelamortquitue.stylux")

# from kivy.app import App
# from kivy.uix.button import Button
#
#
# class TestApp(App):
#     def build(self):
#         return Button(text='Hello World')
#
# TestApp().run()
