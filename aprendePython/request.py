import requests



#TIPOS DE PETICIONES 

# Método HTTP  Llamada
# GET    -- requests.get()

# POST   -- requests.post()

# PUT    -- requests.put()

# DELETE -- requests.delete()

# HEAD  -- requests.head()

# OPTIONS -- requests.options()



#USANDO PARAMETROS PARA HACER PETICIONES 

#Query string => Veamos un ejemplo sencillo. --> Supongamos que queremos 
#buscar paquetes de Python que contengan la palabra «astro»:

# parametro_string = {'q': 'astro'}

# respuesta = requests.get('https://pypi.org', params=parametro_string)

# print(respuesta.url)

#PARAMETRO POST
#acceder a un log in
direccion_url = 'https://giphy.com/login'
my_informacion_login = {'email': 'sdelquin@gmail.com', 'password':'1234'}

respuesta = requests.post(direccion_url, data=my_informacion_login)

print(respuesta.status_code)

# print(respuesta)


















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
