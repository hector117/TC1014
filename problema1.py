def maximo (x,y):
    if x>y:
        return x
    elif y>x:
        return y
    else:
        return ("Ambos números")

#main program below
print ("Problema 1")
print ("Ingresa un número")
x = int(input())
print ("Ingresa el segundo término")
y = int(input())
z = maximo (x,y)
print ("El mayor número de los antes mencionados es:", z)
