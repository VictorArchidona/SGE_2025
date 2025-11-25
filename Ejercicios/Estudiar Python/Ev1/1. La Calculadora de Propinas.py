#Este programa pide al usuario que ingrese una propina que tenga y segun el porcentaje que quiera dejar y las personas
#que van a pagar, calcula cuanto debe dejar cada uno.

def main():

    calcular_propina()


def calcular_propina():

    print("Bienvenido al calculador de propinas.")
    print("--Menu de Propinas--") 

    dinero = float(input("Cuanto dinero tienes: "))
    porcentaje = int(input("Que porcentaje de propina quieres dejar (10, 12, 15...): "))
    personas = int(input("Cuantas personas van a pagar: "))

    dinero_porcentual = (porcentaje / 100) * dinero

    print(f"Cada persona tendra que dejar {dinero_porcentual} euros")

if __name__ == "__main__":
    main()
