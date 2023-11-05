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
        for con in self.encomiendas:
            datos = "ID: {0}, Destinatario: {1}, Direccion: {2}"
            print(datos.format(con.id, con.destinatario, con.direccion))
        print(" ")
    
    def idExiste(self,id):
        existeId = False
        c=0
        for con in self.encomiendas:
            if con.id == id:
                existeId = True
                break
            c += 1
        if existeId:
            indice = c
        else:
            indice = -1
        return indice #retorna -1 si no está, sino, retorna indice en donde está esa id en el arreglo

    def listarEncomienda(self):
        self.listarEncomiendas()
        NumeroCorrecto = False
        while(not NumeroCorrecto):
            idDetalle = input("Ingrese el ID del envío a revisar: ")
            if idDetalle.isnumeric():
                if (int(idDetalle) > 0):
                    NumeroCorrecto = True
                    idDetalle = int(idDetalle)
                else:
                    print("El Id debe ser mayor a 0.")
            else:
                print("debe ingresar un número.")

        existeId=self.idExiste(idDetalle)        
        if existeId == -1:
            idDetalle = 0        
        return idDetalle
        

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

    #método para obtener los datos de un encomienda por teclado

    @staticmethod
    def pedirDatosRegistro(id):
        destinatarioCorrecto = False
        direccionCorrecto = False
        origenCorrecto = False
        destinoCorrecto = False
        while(not destinatarioCorrecto):
            destinatario = input("Ingrese nombre de destinatario: ")
            print(destinatario)
            if destinatario !="":
                destinatarioCorrecto = True
                destinatario = str(destinatario)
            else:
                print("Ingrese un nombre correcto")                        
            
        while(not direccionCorrecto):    
            direccion = input("Ingrese dirección de envío:")
            if direccion !="":
                direccionCorrecto = True
                direccion = str(direccion)
            else:
                print("Ingrese una dirección correcta")                        
        while(not origenCorrecto):                
            c_origen = input("Ingrese ciudad de origen de envío:")
            if c_origen !="":
                origenCorrecto = True
                c_origen = str(c_origen)
            else:
                print("Ingrese ciudad de origen correcto")                        
        while(not destinoCorrecto):    
            c_destino = input("Ingrese ciudad de destino de envío:")
            if c_destino !="":
                destinoCorrecto = True
                c_destino = str(c_destino)
            else:
                print("Ingrese ciudad de destino correcta")                                        
            
        NumeroCorrecto = False
        while(not NumeroCorrecto):
            peso = input("Ingrese peso de envío: ")
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
    
    @staticmethod
    def pedirDatosActDir(id):
    
        direccion = input("Ingrese dirección de envío:")
        destinatario = None
        c_origen = None
        c_destino = None
        peso = None
        encomienda = Encomienda(id, destinatario, direccion, c_origen, c_destino, peso)
        return encomienda

    #métodos para pedir al usuario los datos para usar el CRUD

    def agregarEncomienda(self):
        id=0
        for con in self.encomiendas:
            if con.id > id:
                id = con.id
        encomienda=Courier.pedirDatosRegistro(id+1) #esto asegura que el id es mayor al último registrado
        self.addEncomienda(encomienda) #agrega la encomienda a la lista en el obj
        return encomienda

    def actualizarEncomienda(self):
        self.listarEncomiendas()
        
        NumeroCorrecto = False
        while(not NumeroCorrecto):
            idEditar = input("Ingrese el ID de la encomienda a editar: ")
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
            encomienda=Courier.pedirDatosActDir(idEditar)
            self.encomiendas[existeId]=encomienda #modifica la encomienda en el objeto
        else:
            encomienda = None

        return encomienda


    def eliminarEncomienda(self):
        self.listarEncomiendas()
        
        NumeroCorrecto = False
        while(not NumeroCorrecto):
            idEliminar = input("Ingrese el id de la encomienda a eliminar: ")
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
            del self.encomiendas[existeId] #elimina el registro de la lista en el obj

        return idEliminar
    
    def listarData(self):
        print("\nEncomiendas: \n")
        # for con in self.encomiendas:
        datos = "ID: {0}, Destinatario: {1}, Direccion: {2}, Destinatario: {3}, Destinatario: {4}, Peso: {5} kg"
            # print(datos.format(con.id, con.destinatario, con.direccion, con.c_origen, con.c_destino, con.peso))
        print(datos.format(self.id, self.destinatario, self.direccion, self.c_origen, self.c_destino, self.peso))
