palabra_secreta="chupacabra"

palabra=input("Escribe la palabra secreta: ")
while(True):
    palabra=input("Escribe la palabra secreta: ")
    if palabra==palabra_secreta:
        break
print("Has dejado el bucle con exito")    