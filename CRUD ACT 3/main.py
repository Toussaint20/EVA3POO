from BD.conn import DAO 
#requiere un archivo en carpeta BD con nombre __init__.py 
#(este archivo indica qué importaría de esta carpeta, si está vacío importa todo)
from clase import Courier, Encomienda

def actualizarCourier():
    arrayEncomiendas = dao.listarEncomiendas() #saca los encomiendas de la BD y los deja en un array de tuplas 
    courier.encomiendas=[] #vacía la courier
    for con in arrayEncomiendas: #los pone en el objeto courier como objetos encomienda
       courier.addEncomienda(Encomienda(con[0],con[1],con[2],con[3],con[4],con[5]))

def login():
    continuar = True #continuar = true para que al cerrar sesión vuelva al login
    while continuar:
        print("=== Inicio de Sesión ===")
        usuario = input("Ingrese su ID de usuario: ")
        password = input("Ingrese su contraseña: ")

        resultados = dao.Login(usuario, password)
        if resultados:
            print("=== ¡Inicio de sesión exitoso! ===")
            menuPrincipal()  
        else:
            print("ID de usuario o contraseña incorrectos. Intente nuevamente.")  

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar encomiendas")
            print("2.- Registrar encomienda")
            print("3.- Actualizar dirección de envío de encomienda")
            print("4.- Eliminar encomienda")
            print("5.- Revisar detalle de encomienda")
            print("6.- Cerrar sesión")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 6:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 6:
                continuar = False
                print("¡Gracias por usar la aplicación de Courier!!!")
                actualizarCourier()
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    
    if opcion == 1:
        try:
            #listar
            if len(courier.encomiendas) > 0:
                actualizarCourier()
                courier.listarEncomiendas()
            else:
                print("No se encontraron Encomiendas...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        #registrar
        encomienda = courier.agregarEncomienda()
        try:
            dao.registrarEncomiendas(encomienda.returnArray())
            actualizarCourier()
        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            #actualizar
            if len(courier.encomiendas) > 0:
                encomienda = courier.actualizarEncomienda()              
                
                if encomienda:
                    dao.actualizarEncomiendas(encomienda.returnArray())
                    actualizarCourier()
                else:
                    print("Id de encomienda a actualizar no encontrado...\n")
            else:
                print("No se encontraron encomiendas...")
        except:
            print("Ocurrió un error...")
    elif opcion == 4:
        try:
            #eliminar
            if len(courier.encomiendas) > 0:
                idEliminar = courier.eliminarEncomienda()
                if not(idEliminar == 0):
                    dao.eliminarEncomiendas(idEliminar)
                    
                else:
                    print("Id de encomienda no encontrada...\n")
            else:
                print("No se encontraron encomiendas...")
        except:
            print("Ocurrió un error...")    
    elif opcion == 5:
         try:
            #listar al detalle
            if len(courier.encomiendas) > 0:
                idDetalle = courier.listarEncomienda()
                if not(idDetalle == 0):
                    detalle = dao.listarEncomienda(idDetalle)   
                    print(detalle) 
                else:
                    print("Id de encomienda no encontrada...\n")
            else:
                print("No se encontraron encomiendas...")
         except:
             print("Ocurrió un error...")    
        
    

courier = Courier()
dao = DAO()
actualizarCourier() #ponemos los datos de la BD en el objeto agenda
login()
