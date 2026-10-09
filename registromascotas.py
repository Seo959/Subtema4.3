import os
nombre_mascotas =[""]*3
edad_mascotas =[0]*3

def insertar():
    for i in range(len(nombre_mascotas)):
        nombre_mascotas[i]=input(f"Ingrese el nombre de la mascota: ")
        edad_mascotas[i]=int(input(f"Ingrese edad de la mascota: "))
def mostrar():
    for i in range(len(nombre_mascotas)):
        print(f"Nombre: {nombre_mascotas[i]}, edad: {edad_mascotas[i]}")
def eliminar (nombre_mascota, edad_mascota):
    """ELIMINA UNA MASCOTA EN AMBOS VECTORES"""
    if not nombre_eliminar:
        print("No hay mascota para eliminar")
        return
    nombre_eliminar=input("Ingrese el nombre de mascota a eliminar: ").strip()
    encontrado=False
    i=0
    while i<len(nombre_mascotas):
        if nombre_mascotas[i].lower()==nombre_eliminar.lower():
            nombre_mascotas.pop(i)
            edad_mascotas.pop(i)
            encontrado=True
            print(f"Se eliminó la mascota '{nombre_eliminar}'.")
        else:
            i+=1
        if not encontrado:
            print(f"No se encontró mascota '{nombre_eliminar}'.")
def main ():
    global nombre_mascotas, edad_mascotas 
    nombre_mascotas =[""]*3
    edad_mascotas =[0]*3
    opcion=0
    while opcion !=4:
        os.system('cls' if os.name=='nt' else 'clear')
        print("[1] Insertar Mascota (Nombre | Edad)")
        print("[2] Mostrar Mascotas (Nombre | Edad)") 
        print("[3] Eliminar Mascotas (ambos Vectores)")
        print("[4] SALIR")
        opcion = int(input("Elija una opcion: "))
        if opcion ==1:
            insertar()
        elif opcion ==2:
            mostrar()
        elif opcion==3:
            eliminar()
        elif opcion==4:
            print("SALIENDO....")
        else: print("Opcion Invalida")
        if opcion !=4: input ("Presiona para contunuar....")
main()