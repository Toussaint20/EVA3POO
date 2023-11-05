import hashlib

contraseña = input("¿Cuál es tu contraseña?")

result = hashlib.md5(contraseña.encode())

print("El hexadecimal equivalente al es : ", end ="")
print (result.hexdigest())

if (hashlib.md5(contraseña.encode()).hexdigest() == db_contraseña):
   print("Autentificación exitosa")
else:
   print("Login o Password erroneo")


# si lo quieres probar solo hay que sacar el if y el else
# hay que definir el db_contraseña 
