def numenor (num1, num2):
    if (num1 > num2):
        print ("EL PRIMERO ES MAYOR")
    elif (num2 > num1):
        print ("EL SEGUNDO ES MAYOR")
    elif (num1 == num2):
        print ("SON IGUALES")

num1 = int(input("INTRODUCE EL PRIMER NUMERO"))
num2 = int(input("INTRODUCE EL SEGUNDO NUMERO"))

numenor (num1, num2)