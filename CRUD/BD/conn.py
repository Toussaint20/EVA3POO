import mysql.connector
from mysql.connector import Error

#Data Access Object
class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                database='courier'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))            

    def listarEncomiendas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM Registro ORDER BY Id ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarEncomiendas(self, encomienda):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO Registro (Id, Destinatario, Direccion, C_origen, C_destino, Peso) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')"
                cursor.execute(sql.format(encomienda[0], encomienda[1], encomienda[2], encomienda[3], encomienda[4], encomienda[5]))
                self.conexion.commit()
                print("¡Encomienda registrada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
                self.conexion.rollback()

    def actualizarEncomiendas(self, encomienda):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE registro SET Direccion = {2} WHERE Id = '{0}'"
                cursor.execute(sql.format(encomienda[0], encomienda[2]))
                self.conexion.commit()
                print("¡Dirección de envío actualizada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
                self.conexion.rollback()

    def eliminarEncomiendas(self, codigoEncomienda):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM Registro WHERE Id = '{0}'"
                cursor.execute(sql.format(codigoEncomienda))
                self.conexion.commit()
                print("¡Contacto eliminado!\n")
            except Error as error: #ejemplo de uso de rollback
                print("Fallo al intentar eliminar dato rollback: {}".format(error))
                # revirtiendo los cambios
                self.conexion.rollback()
            finally:
                # closing database connection.
                if self.conexion.is_connected():
                    cursor.close()
                    #conn.close()
                    #print("connection is closed")
            """except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))"""

    def listarEncomienda(self, encomienda):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT * FROM Registro WHERE Id = '{0}'"
                cursor.execute(sql.format(encomienda[0]))
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
                self.conexion.rollback()

    def Login(self, usuario, password):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    sql = "SELECT usuario FROM usuarios WHERE usuario= %s AND password = %s"
                    cursor.execute(sql, (usuario, password))
                    resultados = cursor.fetchall()
                    return resultados
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

#print(mysql.connector.Date(1900,3,23)) #usar constructor de fecha para generar una fecha compatible con la BD