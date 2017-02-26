def hlenword(string):
    l = 0
    for c in string:
        l = l + 1
    return (l)

#main program below
print ("Problema 3")
print ("Ingresa una palabra")
l = input()
print ("El número de carácteres en tu palabra es de", hlenword(l))
