#menu de usuario
op= 0
def mostar_menu():
    print(""" ---MENU PRINCIPAL---
1.-ingresar usuario
2.-buscar usuario 
3.-eliminar usuario
4.-salir""")


while True:
    mostar_menu()
    try:       
        op= int(input("seleccione opcion: "))
        
        if op == 1:
            usuario = input("ingrese Usuario- ")
            
            sexo= input("ingrese sexo- ")
            if sexo >= ("mujer/hombre"):
                print("vuelva a intentar")
        break
    except ValueError:
        print("Debe ingresar M o F solamente. Intente de nuevo.")
                

                    





