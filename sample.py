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

g.add_sommet(u2)

p.add_admin(u2)

print(g)

g.save()
gtest.ouv("lasauvegardedelamortquitue.stylux")

print("-----test ouverture-----")
print(gtest)


# from kivy.app import App
# from kivy.uix.button import Button
#
#
# class TestApp(App):
#     def build(self):
#         return Button(text='Hello World')
#
# TestApp().run()
