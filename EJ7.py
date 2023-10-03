def tributar(edad, ingreso):
    if (edad > 16 and ingreso >= 1000 ):
        print ("TIENES QUE TRIBUTAR")
    else:
        print("NO TIENES QUE TRIBUTAR")

edad = int(input("INTRODUCE TU EDAD: "))
ingreso = int(input("INTRODUCE TUS INGRESOS: "))

tributar (edad, ingreso)