
# Importar librerias necesarias para correr la app
from pyramid.compat import escape
from pyramid.response import Response
from pyramid.view import view_config

# Las funciones view_config le dicen a Pyramid qué vista de ruta se va a definir en la función que sigue

@view_config(route_name='intro')
def home_page(request):
    header = '<h2 style="text-align: center;">Home Page</h2>'
    body = '<br><br><p style="text-align: center; font-family: verdana; color: purple;">HOLA, MI NOMBRE ES FERNANDO.</p>'
    body += '<p style="text-align: center; font-family: verdana;"> Esta es mi segunda app de pyramid.</p>'
    footer = '<p style="text-align: center; font-family: verdana;">Para <a href="/fer">mas información</a>.</p>'

    # En la etiqueta 'a', observe que href contiene '/ fer', esta ruta se definirá en el archivo intro.py
    # Simplemente le dice a la vista que navegue a esa ruta y ejecute cualquier código que esté en esa vista

    return Response(header + body + footer)

@view_config(route_name='fer')
def fer_history(request):
    header = '<h2 style="text-align: center;">Fernando Hernadez Vazquez</h2>'
    job1 = '<p style="text-align: center; font-family: verdana;">Universidad tecnologica de Tulancingo</p><p style="text-align: center">HOLAA</p>'

    return Response(header + job1)