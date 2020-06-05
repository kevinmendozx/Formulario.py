#conexion a la base de datos
import pyodbc 

def Autenticacion(Usuario,password):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}', server='.', database='Warehouse',               
               trusted_connection='yes')
    cursor = cnxn.cursor()
    #Envio de query
    cursor.execute("SELECT * FROM usuario where upper(usuario) = %s and upper(pass) = %s " %(usuario,passs))

    #Carga respuesta de la query en lista
    row = cursor.fetchone() 
    #cierre de conexion a la base de datos
    cnxn.close()

    mensaje ="No existe usuario"
    flag = 0
    if row is not None:
            mensaje = "Existe el usuario"
            flag = 1
    return(mensaje,flag)
    

estado = 0

while estado == 0:
    #Ingreso de datos
    print("Ingrese su usuario")
    usuario ="'"+input().upper()+"'"
    print("Ingrese su contraseña")
    passs = "'"+input().upper()+"'"

    #imprime el mensaje que envia la funcion
    mensajes,estados = Autenticacion(usuario,passs)
    print(mensajes)

    if estados == 0:
        print("Ingreso mal los datos, vuelva a ingresarlo")
    else:
        estado = estados



