edad = int(input("Escriba su edad:"))
if edad < 18:
    print("Debes ser mayor de edad.")
else:
    nivel_fisico = int(input("Escriba su nivel físico con números del 1-10:"))
    if nivel_fisico not in range(1,11):
        print("El valor debe estar situado entre 1-10")
    elif nivel_fisico < 5:
        print("Debes estar en mejor forma:")
    else:
        print("¡Listo para despegar!")