from Subasta.Usuari import Usuari
from Subasta.Subhasta import Subhasta

u = Usuari("Toni", 100)
u2 = Usuari("Pep", 150)
u3 = Usuari("Enric", 300)
s = Subhasta("Telèfon Mòbil", u)

print("\nSubhasta 1")
s.pujar(u2, 100)
print(s.getPujaAlta().getUserName() + " " + str(s.getPujaAlta().getPuja()))
s.pujar(u3, 50)
s.executar()
s.pujar(u3, 200)

print("\nSubhasta 2")
s1 = Subhasta("Impresora 3D", u2)
s1.pujar1(u3)
s1.executar()

usuaris = list()
usuaris.append(u)
usuaris.append(u2)
usuaris.append(u3)
print("\nUsuarios/Dinero")
for n in usuaris:
    print(n.getNombre() + " " + str(n.getCredito()))

print("\nUsuarios/subhasta")
for n in usuaris:
    for s in n.getSubHastas():
        print(n.getNombre() + " " + s.getProducto())
