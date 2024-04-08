import requests


# Realizar peticionn HTTP 
response = requests.get("https://pypi.org/")

type(response)
print(response.text)



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
