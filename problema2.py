def max_of_three(x,y,z):
    if x>y & x>z:
        return x
    elif y>z & y >x:
        return y
    elif z>x & z>y:
        return z
    elif x==y & x>z:
        return (x, "y",y"son los mayores")
    elif x==z & x>z:
        return (x, "y",z"son los mayores")

#main program below
print ("Problema 2")
print ("Ingresa un número")
x = int(input())
print ("Ingresa otro número")
y = int(input())
print ("Ingresa el último número")
z = int(input())
a = max_of_three (x,y,z)
print ("El mayor de tus números es:", a)
