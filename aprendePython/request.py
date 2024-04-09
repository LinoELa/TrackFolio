import requests

#optener la cabecera 

pagina = requests.get('https://casaruralzaragoza.com/')
# print(pagina.text)

print(pagina.url)
print(pagina.status_code)

print(pagina.headers.get('Content-Type'))
print(pagina.headers.get('Server'))


