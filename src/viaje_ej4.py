distancia_marte = 225000000
for velocidad in range (10000,60000,10000):
    tiempo = (distancia_marte/velocidad)/24
    print(f"Velocidad: {velocidad} km/h -> Tiempo: {tiempo} días" )