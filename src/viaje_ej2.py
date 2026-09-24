distancia_km = int(input("¿Que distancia deberá recorrer el cohete?:"))  # distancia Tierra - Luna
velocidad_kmh = int(input("¿Que velocidad deberá mantener el cohete?:"))
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {tiempo_dias} días en llegar.")