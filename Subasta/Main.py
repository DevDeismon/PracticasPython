from Subasta.Usuari import Usuari
from Subasta.Subhasta import Subhasta

u = Usuari("Toni", 100)
u2 = Usuari("Pep", 150)
u3 = Usuari("Enric", 300)
s = Subhasta("Telèfon Mòbil", u)

s.pujar(u2, 100)
print(s.getPujaAlta().getUserName() + " " + str(s.getPujaAlta().getPuja()))
s.pujar(u3, 50)
