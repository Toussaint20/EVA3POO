from BD.conn import DAO 
#requiere un archivo en carpeta BD con nombre __init__.py 
#(este archivo indica qué importaría de esta carpeta, si está vacío importa todo)

from clase import Courier, Encomienda

def actualizarCourier():
    arrayEncomiendas = dao.listarEncomiendas() #saca los encomiendas de la BD y los deja en un array de tuplas 
    courier.encomiendas=[] #vacía la courier
    for enc in arrayEncomiendas: #los pone en el objeto courier como objetos encomienda
        courier.addEncomienda(Encomienda(enc[0],enc[1],enc[2]))

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
            print("5.- Buscar una encomienda")
            print("6.- Salir")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 6:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 6:
                continuar = False
                print("¡Gracias por usar la aplicación de Courier!!!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    
    if opcion == 1:
        try:
            #actualizarcourier()
            if len(courier.encomiendas) > 0:
                courier.listarEncomiendas()
            else:
                print("No se encontraron Encomiendas...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        encomienda = courier.agregarEncomienda()
        try:
            dao.registrarEncomienda(encomienda.returnArray())
        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            #actualizarcourier()
            if len(courier.encomiendas) > 0:
                encomienda = courier.actualizarEncomienda()
                if encomienda:
                    dao.actualizarEncomienda(encomienda.returnArray())
                else:
                    print("Id de encomienda a actualizar no encontrado...\n")
            else:
                print("No se encontraron encomiendas...")
        except:
            print("Ocurrió un error...")
    elif opcion == 4:
        try:
            #actualizarcourier()
            if len(courier.encomiendas) > 0:
                idEliminar = courier.eliminarEncomiendas()
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
            #actualizarcourier()
            if len(courier.encomiendas) > 0:
                courier.listarEncomienda()
            
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")
        
    

courier = Courier()
dao = DAO()
actualizarCourier() #ponemos los datos de la BD en el objeto agenda

menuPrincipal()
