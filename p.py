# 165 248 94 346 299 73 198 221 313 137 205 87 336 110 186 69 223 213 216 216 177 138  
#Modulo 37

mensaje = "17 26 20 13 3 36 13 36 17 26 20 13 3 36 1 32 1 28 31 31 29 27"
decifrado = ""

for a in mensaje.split():
    num = int(a)
    if 0 <= num <= 25:
        caracter = chr( 65 + num)
    elif 26 <= num <= 35:
        caracter = str(num - 26)
    elif num == 36:
        caracter = '_'

    decifrado+= caracter
flag=  decifrado
print(flag)
flagFinal="picoCTF{"+flag+"}"
print(flagFinal)
