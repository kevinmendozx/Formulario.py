def Autenticacion(Usuario,password):
        mensaje ="No existe usuario"
        if row is not None:
            mensaje = "Existe el usuario"
        return(mensaje)
#conexion a la base de datos
import pyodbc
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}', server='.', database='Warehouse',               
               trusted_connection='yes')
cursor = cnxn.cursor()

#Ingreso de datos
print("Ingrese su usuario")
usuario ="'"+input().upper()+"'"
print("Ingrese su contraseña")
passs = "'"+input().upper()+"'"
#Envio de query
cursor.execute("SELECT * FROM usuario where upper(usuario) = %s and upper(pass) = %s " %(usuario,passs))

row = cursor.fetchone() 
print(Autenticacion(usuario,passs))

#cierre de conexion a la base de datos
cnxn.close()
