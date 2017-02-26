def tf(string):
    l=""
    for c in string:
        if c in ["a","e","i","o","u"]:
            l= l + c + " True"
        else:
            l = l + c + " False"
        return (l)

#main program below
print ("Problema 4")
print ("Ingresa una letra")
l = input()
print (tf(l))
