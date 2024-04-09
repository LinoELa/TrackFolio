import requests


# Realizar peticionn HTTP 
respuesta = requests.get("https://pypi.org/")

# print(type(response))
# print(response.text)


#Algo que es realmente importante en una petición HTTP es comprobar
# el estado de la misma. Por regla general, si todo ha ido bien, 
#deberíamos obtener un código 200, pero existen muchos otros códigos de estado 
#de respuesta HTTP:

print(respuesta.status_code)

#para avitar un acomparacion directa con 200 se puede usar 
print(respuesta)



















# import requests

# # Hacer una solicitud GET a una URL
# url = 'https://casaruralzaragoza.com/'
# response = requests.get(url)

# # Verificar si la solicitud fue exitosa (código de estado 200)
# if response.status_code == 200:
#     # Imprimir el contenido de la respuesta
#     print(response.text)
# else:
#     # Imprimir un mensaje de error si la solicitud falló
#     print('Error:', response.status_code)
