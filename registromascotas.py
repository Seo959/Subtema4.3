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
def eliminar(nombreborrar):
    for i in range(len(nombre_mascotas)):  
      if nombre_mascotas[i]==nombreborrar:
        for j in range(i,len(nombre_mascotas)-1):
            nombre_mascotas[j]=nombre_mascotas[j+1]
            edad_mascotas[j]=edad_mascotas[j+1] 
                
        nombre_mascotas[-1] = ""
        edad_mascotas[-1] = 0
        print(f"Mascota Eliminada {nombreborrar}")        
  
        
        
def main ():
    global nombre_mascotas, edad_mascotas 
    nombre_mascotas =[""]*3
    edad_mascotas =[0]*3
    opcion=0
    while opcion !=5:
        os.system('cls' if os.name=='nt' else 'clear')
        print("[1] Insertar Mascota (Nombre | Edad)")
        print("[2] Mostrar Mascotas (Nombre | Edad)") 
        print("[3] Eliminar Mascotas (ambos Vectores)")
        print("[4] Ordenar alfabeticamente)")
        print("[5] SALIR")
        opcion = int(input("Elija una opcion: "))
        if opcion ==1:
            insertar()
        elif opcion ==2:
            mostrar()
        elif opcion ==3:
            mascotaborrar= input("ingrese mascota a borrar :")
            eliminar(mascotaborrar)
        elif opcion ==4:
            ordenar()
        elif opcion==5:
            print("SALIENDO....")
        else: print("Opcion Invalida")
        if opcion !=5: input ("Presiona para continuar....")
main()