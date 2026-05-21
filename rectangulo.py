def rectangle(alto,ancho):
    for i in range (1, ancho+1):
     print("#",end=" ")
    for j in range(1, alto):
            print("#")
            for k in range(1,ancho+1):
                print(" ",end=" ")
            print("#")   
    for i in range (1, ancho):
     print("#",end=" ") 
                
         

rectangle(25,50)