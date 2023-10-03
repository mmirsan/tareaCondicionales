def ingresa(dia):
    if (dia == "lunes"):
        print("ES LUNES")
    elif (dia == "viernes"):
        print ("YA ES VIERNES!!")
    elif (dia == "sabado" or dia == "domingo"):
        print ("YA ES FIN DE SEMANA!!")
        
dia = input("INTRODUCE UN DIA DE LA SEMANA: ")

ingresa (dia)