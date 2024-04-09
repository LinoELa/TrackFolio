import requests


# CONTENIDO JSON

sc_tnerife = (28.4578025, -16.3563748)

parametros_1 = {
    'latitude' : sc_tnerife[0], 
    'longitude' : sc_tnerife[1], 
    'hourly' : 'temperature_2m'
    }

url_del_api = 'https://api.open-meteo.com/v1/forecast'

respuesta = requests.get(url_del_api, params=parametros_1)

print(respuesta.url)

datos = respuesta.json()
# print(datos)
# dict
print(datos.keys())



# QUEREMOS MOSTRAR DE DE UN SOLO DIA 

temperaturas = datos['hourly']['temperature_2m']

for i, temp in enumerate(temperaturas[24:48], start=1):
    print(f'{temp:4.1f}', end='---')
    if i % 6 == 0 :
        print()


