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

# LOCALIZAR UNICO ELEMENTO

#elemento que no existe

elemento_unico_form = sopa.find('form')
# print(elemento_unico_form)


#elemento que existe
elemento_unico_no_existe = sopa.find('strange-tag')
# print(elemento_unico_no_existe)


#Multiples 'li'. Solo devuelve el primero
elemento_unico_li = sopa.find('li')
# print(elemento_unico_li)


#LOCALIZAR DESDE ELEMENTO
elemento_desde_un_bloque = sopa.find_all('div', 'block') [1]
# print(elemento_desde_un_bloque)

elemento_desde_un_bloque_2 = sopa.find_all('h2')
# print(elemento_desde_un_bloque_2)

#OTRAS FUNCIONES 

#Localizar los <<div>> o elemetos "superiores" apartir de un elemento concreto de su clase.

gold = sopa.find('li', 'gold')
# print(gold)

gold_parent = gold.find_parents('div')
# print(gold_parent)

#Localizar elementos hermanos siguientes
blue_li = sopa.find('li' , 'blue') #localizar elemento
# print(blue_li)

blue_li_parents = blue_li.find_next_sibling() #localizar elemento siguiente
# print(blue_li_parents)



#localizar todos los elementos acontinuacion de uno dado:

elemento_a_continuacion = sopa.find('input', type='submit')
# print(elemento_a_continuacion)

elemento_a_continuacion_submit = elemento_a_continuacion.find_all_next()
# print(elemento_a_continuacion_submit)


#localizar todos los elementos previos a uno dado.
ul_data = sopa.find('ul', id='data')
# print(ul_data)

ul_data_previo = ul_data.find_all_previous(['h1', 'h2'])
# print(ul_data_previo)

ul_data_previo_parents = ul_data.find_parents(['h1, h2'])
# print(ul_data_previo_parents)


#ATAOS DE BUSQUEDAS 
busqueda = sopa.find_all('span')
# print(busqueda)

atajo_busqueda = sopa('span')
print(atajo_busqueda)














