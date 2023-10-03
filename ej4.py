def numenor (num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        print ("EL PRIMERO ES MAYOR")
    elif (num2 > num1 and num2 > num3):
        print ("EL SEGUNDO ES MAYOR")
    elif (num3 > num1 and num3 > num2):
        print ("EL TERCER NUMERO ES MAYOR")

num1 = int(input("INTRODUCE EL PRIMER NUMERO"))
num2 = int(input("INTRODUCE EL SEGUNDO NUMERO"))
num3 = int(input("INTRODUCE EL TERCER NUMERO"))
numenor (num1, num2, num3)