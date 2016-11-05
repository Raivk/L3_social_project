from socialnet.Graphe import Graphe,Sommet,Utilisateur,Page

g = Graphe()
u = Utilisateur("Perroni","Pep",50)
p = Page("DogeLand.com")

g.add_sommet(u)
g.add_sommet(p)
u.connect(p)

print(g)
print(u)
print(p)
print("------------")

u.disconnect(p)

print(u)

# from kivy.app import App
# from kivy.uix.button import Button
#
#
# class TestApp(App):
#     def build(self):
#         return Button(text='Hello World')
#
# TestApp().run()
