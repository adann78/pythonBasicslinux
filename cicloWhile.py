
counter=0   
while counter<=5:
    print("Numero",counter)
    counter+=1
else:
    print("El ciclo ha terminado")

response=""
while response.lower()!="salir":
    response=input("Escribe'salir' para finalizar el programa: ")
else:
    print("Has salido del programa")