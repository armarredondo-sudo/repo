"""producto{
1. Agregar producto 
2. Mostrar productos 
3. Buscar producto 
4. Producto mas caro 
5. Salir
}"""

def agregar_profucto(productos):
    nombre = input ("nombre del producto: ").strip()

    if nombre == "":
        print("El nombre no puede ser vacio")
        return
    if nombre in productos:
        print("el producto ya existe")
        return
    
    stock = int(input ("ingrese stock: "))
    precio= int(input ("ingrese precio: "))

    productos(nombre) = [stock,precio]
    print("Producto agregado correctamente")
 


productos={}

while True:
    print("---Menu---")
    print("1. Agregar producto ")
    print("2. Mostrar productos ")
    print("3. Buscar producto ")
    print("4. Producto mas caro ")
    print("5. Salir")

    while True:
        try:
            
            op= int(input("selecciones opcion: "))
            break
        except ValueError:
            print("error, debe ingresar un numero entre 1 y 5, intente nuevamente")

    if op == 1:
        agregar_producto(productos) 

    elif op == 2:
        mostrar_producto(productos) 

    elif op ==3:
        buscar_producto(productos) 

    elif op ==4:
        producto_mas_caro(productos) 

    elif op== 5:
        print("fin del programa")
        break
    else:
        print("opcion invalida!")
