import requests

#   DESCARGAR FICHEROS


# fichero en texto plano
        #se crea un ficchero data.csv y se le escribe dentro
url_fichero_plano = 'https://www.ine.es/jaxi/files/tpx/es/csv_bdsc/50155.csv'

pagina = requests.get(url_fichero_plano)

pagina.status_code


with open('data.csv' , 'w') as f : 
    f.write(pagina.text)


#Fichero Binario

url_fichero_binario = 'https://www.ine.es/jaxi/files/tpx/es/csv_bdsc/50155.csv'

pagina_2 = requests.get(url_fichero_binario)

pagina_2.status_code

with open('datos_fichero_binario', 'w') as f:
    f.write(pagina_2.content) #
            # TypeError: write() argument must be str, not bytes


            




