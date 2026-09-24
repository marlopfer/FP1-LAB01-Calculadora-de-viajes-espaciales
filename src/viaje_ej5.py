distancia_km = int(input("¿Que distancia deberá recorrer el cohete?:"))  # distancia Tierra - Luna
velocidad_kmh = int(input("¿Que velocidad deberá mantener el cohete?:"))
repeticion = True
while repeticion:
    tiempo_horas = distancia_km // velocidad_kmh
    tiempo_dias = tiempo_horas // 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    respuesta = str(input("¿Desea repetir la simulación: s/n?")).lower()
    if respuesta == str('n'):
        break
    else:
        repeticion: True
        distancia_km = int(input("¿Que distancia deberá recorrer el cohete?:"))
        velocidad_kmh = int(input("¿Que velocidad deberá mantener el cohete?:"))