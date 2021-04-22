TIPOA="A"
TIPOB="B"
PRECIOA=100
PRECIOB=200
TAMAÑO=1
TAMAÑO=2
def calculoPrecio(tipo,tamaño,cantidad):
    precio=0
    if tipo==TIPOA or tipo==TIPOB:
        if tipo==TIPOA:
            precio=PRECIOA
        elif tipo==TIPOB:
            precio=PRECIOB
    else:
        print("F")
def main():
    precioFinal=0
    print("Venta de Uvas")
    tipo=input("Selecciona un tipo(A/B): ")
    tamaño=input("Selecciona un tamaño(1/2):")
    cantidad=input("Selecciona una cantidad: ")

    print("Precio final es de "+precioFinal+"€")
