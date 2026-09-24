distancia = int(input("Escriba la distancia a recorrer:"))
parada = 0
for i in range(0,distancia,150000):
        parada +=1 
        print (f"Parada en el km {i}")
if i < distancia:
    print(f"Total de paradas para repostar:{parada}")