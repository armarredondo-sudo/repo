bd_estudiantes=[]

def mostar_menu():
    print("...menu...")
    print("1.agregar estudiante")
    print("2.buscar estudiante")
    print("3.eliminar estudiante")
    print("4.actualizar estudiante")
    print("5.mostrar estudiante")
    print("6.sali")

def leer_opcion():
    opcion = input ("---> ")
    if opcion in (1, 2, 3, 4, 5, 6):
        return int(opcion)
    return False

def validar_nombre(nombre):
    if len(nombre.strip())> 0:
        return True
    return False
def valida_nota(nota):
    try:
        numero = float(nota)
        if 1.0 <= numero <=7.0:
            return True
        return False
    except ValueError:
        return False
    
def validar_edad(edad):
    if edad.isdigit() and int(edad)>0:
        return True
    return False

def agregar_estudiante(lista):
    nombre = input("ingresar el nombre completo")
    if validar_nombre(nombre) == False:
        print(" el nombre no puede estar vacio")
        return
    edad= input("ingresar edad")
    if validar_edad(edad):
        print("la edad ")
        return
    nota= input("(1.0 a 7.0)\ningresar la nota: ")
    if valida_nota(nota) == False:
        print("la nota debe ser entre 1.0 a 7.0")
        return
    
    estudiante={"nombre": nombre,
                "edad": int(edad),
                "nota": float(nota), 
                "aprobado": False
            }
    lista.append(estudiante)
    print("estudiante registro con exito")

def buscar_estudiantes(lista):
    for estudiante in lista:
        if estudiante["nota"] >= 4.0:
            estudiante["aprobado"] = True
        else:
            estudiante["aprobado"] = False

def mostrar_estudiante(lista):
    actualizar_estado(lista)

    if len(lista) ==0:
        print("")
        return

    print(" ")
    for estudiante in lista["aprobado"]== True:
        estado="aprobado"
    else:
        estado="reprobado"
