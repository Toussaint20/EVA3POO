class Encomienda():
    def __init__(self,id,destinatario, direccion, c_origen, c_destino, peso):
        self.id = id
        self.destinatario = destinatario
        self.direccion = direccion
        self.c_origen = c_origen
        self.c_destino = c_destino
        self.peso = peso

    
    #método para entregar datos a la BD
    def returnArray(self): 
        return [self.id,self.destinatario,self.direccion,self.c_origen,self.c_destino,self.peso]

class Courier():
    
    encomiendas=[]

    #metodos que obtienen datos

    def listarEncomiendas(self):
        print("\nEncomiendas: \n")
        for enc in self.encomiendas:
            datos = "ID {0}, Destinatario: {1}, Direccion {2}, C_origen {3}, C_destino {4}, Peso {5}"
            print(datos.format(enc.id, enc.destinatario, enc.direccion))
        print(" ")
    
    def idExiste(self,id):
        existeId = False
        c=0
        for enc in self.encomiendas:
            if enc.id == id:
                existeId = True
                break
            c += 1
        if existeId:
            indice = c
        else:
            indice = -1
        return indice #retorna -1 si no está, sino, retorna indice en donde está esa id en el arreglo

    def listarEncomienda(self,encomienda):
        print("\nEncomienda: \n")
        for enc in self.encomienda:
            datos = "ID {0}. Destinatario: {1}, Direccion {2}"
            print(datos.format(enc.id, enc.destinatario, enc.direccion))
        print(" ")

    #métodos que modifican el Courier

    def addEncomienda(self,encomienda):
        self.encomiendas.append(encomienda)
    
    def delEncomienda(self,id):
        c=0
        for re in self.encomiendas:
            if re.id == id:
                del self.encomiendas[c]
                break
            c += 1

    #método para obtener los datos de un contacto por teclado

    @staticmethod
    def pedirDatosRegistro(id):
    
        destinatario = input("Ingrese nombre de destinatario: ")
        direccion = input("Ingrese dirección de envío:")
        c_origen = input("Ingrese ciudad de origen de envío:")
        c_destino = input("Ingrese ciudad de destino de envío:")
        peso = input("Ingrese peso de envío:")
        NumeroCorrecto = False
        while(not NumeroCorrecto):
            peso = input("Ingrese Número Telefónico: ")
            if peso.isnumeric():
                if (int(peso) > 0 and len(peso)<10):
                    NumeroCorrecto = True
                    peso = int(peso)
                else:
                    print("El número debe ser mayor a 0 y de 9 dígitos máximo.")
            else:
                print("Número incorrecto: Debe ser un número Únicamente.")
        encomienda = Encomienda(id,destinatario, direccion, c_origen, c_destino, peso)
        return encomienda

    #métodos para pedir al usuario los datos para usar el CRUD

    def agregarEncomienda(self):
        id=0
        for enc in self.encomiendas:
            if enc.id > id:
                id = enc.id
        encomienda=Courier.pedirDatosRegistro(id+1) #esto asegura que el id es mayor al último registrado
        self.addEncomienda(encomienda) #agrega al contacto a la lista en el obj
        return encomienda

    def actualizarEncomienda(self):
        self.listarEncomiendas()
        
        NumeroCorrecto = False
        while(not NumeroCorrecto):
            idEditar = input("Ingrese el ID del contacto a editar: ")
            if idEditar.isnumeric():
                if (int(idEditar) > 0):
                    NumeroCorrecto = True
                    idEditar = int(idEditar)
                else:
                    print("El Id debe ser mayor a 0.")
            else:
                print("debe ingresar un número.")
        
        existeId=self.idExiste(idEditar)

        if existeId > -1:
            print("ingrese datos a modificar")
            encomienda=Courier.pedirDatosRegistro(idEditar)
            self.encomiendas[existeId]=encomienda #modifica el contacto en el objeto
        else:
            encomienda = None

        return encomienda


    def eliminarEncomienda(self):
        self.listarEncomiendas()
        
        NumeroCorrecto = False
        while(not NumeroCorrecto):
            idEliminar = input("Ingrese el id del contacto a eliminar: ")
            if idEliminar.isnumeric():
                if (int(idEliminar) > 0):
                    NumeroCorrecto = True
                    idEliminar = int(idEliminar)
                else:
                    print("El Id debe ser mayor a 0.")
            else:
                print("debe ingresar un número.")

        existeId=self.idExiste(idEliminar)

        if existeId == -1:
            idEliminar = 0
        else:
            del self.encomiendas[existeId] #elimina el contacto de la lista en el obj

        return idEliminar
