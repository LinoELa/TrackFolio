# Para empezar a trabajar con Beautiful Soup es necesario construir un objeto de tipo BeautifulSoup que reciba el contenido a «parsear»:


#EJEMPLO A PEQUENA ESCALA CON CODICO INTERNO

from bs4 import BeautifulSoup
# from requests import get

contenido = """
<html lang="en">
<head>
    <title>Just testing</title>
</head>
<body>
    <h1>Just testing</h1>
    <div class="block">
      <h2>Some links</h2>
      <p>Hi there!</p>
      <ul id="data">
        <li class="blue"><a href="https://example1.com">Example 1</a></li>
        <li class="red"><a href="https://example2.com">Example 2</a></li>
        <li class="gold"><a href="https://example3.com">Example 3</a></li>
      </ul>
    </div>
    <div class="block">
      <h2>Formulario</h2>
      <h2>Formulario secundario</h2>
      <form action="" method="post">
        <label for="POST-name">Nombre:</label>
        <input id="POST-name" type="text" name="name">
        <input type="submit" value="Save">
      </form>
    </div>
    <div class="footer">
      This is the footer
      <span class="inline"><p>This is span 1</p></span>
      <span class="inline"><p>This is span 2</p></span>
      <span class="inline"><p>This is span 2</p></span>
    </div>
</body>
</html>
"""


sopa = BeautifulSoup(contenido, features='html.parser')

#ACCEDER AL CONTENIDO

#Nombre de etiqueta --> Ver el nomrbe de la etiqueta
nombre = sopa.name
# print(nombre)

elem = sopa.find('ul', id='data')
# print(elem.name)

elem = sopa.find('h1')
# print(elem.name)


#ACCESO A ATRIBUTOS

elem = sopa.find('input', id='POST-name')
# print(elem)

name_elem = elem['id']
# print(name_elem)

name_elem = elem['name']
# print(name_elem)

name_elem = elem['type']
# print(name_elem)

#Acceder a los diccionarios completos de atributos 
elem_dict = elem.attrs
print(elem_dict)

#contenido textual 

footer = sopa.find(class_='footer')
# print(footer)

footer_text = footer.text
# print(footer_text) #Imprime solo el texto 

footer_list = list(footer.strings)
# print(footer_list) #imprime solo la lista 


footer_list = list(footer.stripped_strings)
# print(footer_list) #imprime solo la lista 

footer_list = footer.span.string
print(footer_list)

footer_list = footer.string
# print(footer_list)






















