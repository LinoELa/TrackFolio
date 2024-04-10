# TrackFolio
https://aprendepython.es/pypi/scraping/beautifulsoup/
## BS4

<!-- Parte 1  -->
### Haciendo sopa 
He tennid un problem con el nombre del archivo poque le he puesto un numero "bs4.py" asi que no me lo leia bien. 

He tenenido que cambiar a "bsoup.py" y a funcionado , el error decia :

"    

from bs4 import BeautifulSoup
ImportError: cannot import name 'BeautifulSoup' from partially initialized module 'bs4' (most likely due to a circular import) (/Users/ela/Desktop/DEVELOPER/TrackFolio/aprendePython/Bs4/bs4.py)

"


Hasta ahora hemos visto las funciones find_all() y select() que localizan un conjunto de elementos. Incluso en el caso de encontrar sólo un elemento, se devuelve una lista con ese único elemento.

Se podría decir que la función find_all() busca en descendientes y que la función find_parents() busca en ascendientes.

Contenido textual
Es necesario aclarar las distintas opciones que proporciona Beautiful Soup para acceder al contenido textual de los elementos del DOM.

Atributo

Devuelve

text

Una cadena de texto con todos los contenidos textuales del elemento incluyendo espacios y saltos de línea

strings

Un generador de todos los contenidos textuales del elemento incluyendo espacios y saltos de línea

stripped_strings

Un generador de todos los contenidos textuales del elemento eliminando espacios y saltos de línea

string

Una cadena de texto con el contenido del elemento, siempre que contenga un único elemento textual

Además de localizar elementos, este paquete permite moverse por los elementos del DOM de manera muy sencilla.

## Moverse hacia abajo
Para ir profundizando en el DOM podemos utilizar los nombres de los «tags» como atributos del objeto, teniendo en cuenta que si existen múltiples elementos sólo se accederá al primero de ellos:




