def traductor(l):
    x=""
    for c in l:
        if c in ("a","e","i","o","u"):
            x += c
        else:
            x += c + "o" + c
    return x

#main program below
print ("Problema 5")
print ("Ingresa una palabra o frase")
l = input()
print("La traducción es:")
print(traductor(l))
