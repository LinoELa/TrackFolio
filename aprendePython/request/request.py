import requests

#   NOMBRE DE FICHEROS

url_fichero_plano = 'https://www.ine.es/jaxi/files/tpx/es/csv_bdsc/50155.csv'

pagina = requests.get(url_fichero_plano)


def obtener_filename(pagina):
    try:
        return pagina.headers['Content-Disposition'].split(',').split('=')[1]
    except(KeyError, IndexError):
        return pagina.url.split('/')[-1]
    
