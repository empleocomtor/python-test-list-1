from masrepetidas import masrepetidas


lista_1 = []
lista_2 = ["mico", "gato", "mico", "oso", "perro"]
lista_3 = ["perro", "perro", "perro", "perro", "perro"]
lista_4 = ["oso", "oso", "oso", "oso", "oso"]
lista_5 = [" ", "mico", "gato", "oso", " " ,"toro", "iguana", "gallo"]
lista_6 = ["gato", "gato", "mico", "mico","gato","oso" "mico", "perro", "gato"]
lista_7 = ["loro", "mico", "gallo", "gato", "cocodrilo", "perro", "loro"]
lista_8 = ["iguana", "mono", "iguana", "iguana", "iguana", "iguana", "oso", "gato", "gato", "lagarto", "lagarto", "gatorade"]
lista_9 = ["gallo", "gallo", "gallo", "gallo", "gato", "mono", "perro","mico", "oso", "perro", " ", " ", " "]
lista_10 =["vaca", "toro", "iguana", "gallo", "gato", "mono", "perro", "foca", "lagarto", "vaca", "toro"]

contador = 0
resp1 = masrepetidas(lista_1)
if resp1 is not None :
    print ("FALLO_LA_PRUEBA_1")
else: 
    contador = contador +1 

resp2 = masrepetidas(lista_2)
if resp2 != "mico":
    print ("FALLO_LA_PRUEBA_2")
else: 
    contador = contador +1 

resp3 = masrepetidas(lista_3)
if resp3 != "perro":
    print ("FALLO_LA_PRUEBA_3")
else: 
    contador = contador +1 

resp4 = masrepetidas(lista_4)
if resp4 != "oso":
    print ("FALLO_LA_PRUEBA_4")
else: 
    contador = contador +1 

resp5 = masrepetidas(lista_5)
if resp5 != " ":
    print ("FALLO_LA_PRUEBA_5")
else: 
    contador = contador +1 

resp6 = masrepetidas(lista_6)
if resp6 != "gato":
    print ("FALLO_LA_PRUEBA_6")
else: 
    contador = contador +1 

resp7 = masrepetidas(lista_7)
if resp7 != "loro":
    print ("FALLO_LA_PRUEBA_7")
else: 
    contador = contador +1 

resp8 = masrepetidas(lista_8)
if resp8 != "iguana":
    print ("FALLO_LA_PRUEBA_8")
else: 
    contador = contador +1 

resp9 = masrepetidas(lista_9)
if resp8 != "gallo":
    print ("FALLO_LA_PRUEBA_9")
else: 
    contador = contador +1 

resp10 = masrepetidas(lista_10)
if resp10 != "vaca" and resp10 != "toro":
    print ("FALLO_LA_PRUEBA_10")
else: 
    contador = contador +1 

print("La cantidad de respuestas correctas es" , contador)