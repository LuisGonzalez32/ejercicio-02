from ingresos import ingresos
from egresos import egresos



Ingresos = ingresos()
Egresos = egresos()

while True:

    print("presione 1 para poner sus ingresos")
    print("presione 2 para poner sus egresos")
    print("presione 3 para ver su informe")
    opcion = int(input(" "))

    

    if opcion == 1:
        ingresos = int(input("ponga el monto que quiere poner: "))

        

        Ingresos.aumentarIngresos(ingresos)
        

        var = Ingresos.getMontoTotal()


        print(f"Ahora el monto total es {var}")
        print("")

    elif opcion == 2:

        var = int(var)
        egresos = int(input("ponga el monto que quiere sacar: "))
        
        #if egresos > var:
         #   print("no puede sacar tanto dinero porque no tiene tanto")
        #else:
        Egresos.aumentarEgresos(egresos)
        ingre = Ingresos.getMontoTotal()
        egre = Egresos.getMontoTotal()

        total = ingre - egre


        print(f"ahora su total es {total}")

    elif opcion == 3:


        print(f"sus ingresos son {ingre}")
        print(f"sus egresos son -{egre}")

        print(f"su balance es de {total}")

        print("-"*100)


    