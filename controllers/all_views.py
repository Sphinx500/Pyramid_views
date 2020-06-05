# all_views.py
# Import necessary functions to run our web app
from pyramid.compat import escape
from pyramid.response import Response
from pyramid.view import view_config

# view_config functions tells Pyramid which route's view is going to be defined in the function that follows
# the name of the function does not matter, you can name it whatever you like

@view_config(route_name='intro')
def home_page(request):
    header = '<h2 style="text-align: center;">Home Page</h2>'
    body = '<br><br><p style="text-align: center; font-family: verdana; color: purple;">HOLA, MI NOMBRE ES FERNANDO.</p>'
    body += '<p style="text-align: center; font-family: verdana;"> Esta es mi segunda app de pyramid.</p>'
    footer = '<p style="text-align: center; font-family: verdana;">Para <a href="/fer">mas información</a>.</p>'

    # In the 'a' tag, notice that the href contains '/jobs', this route will be defined in the intro.py file
    # It is simply telling the view to navigate to that route, and run whatever code is in that view

    return Response(header + body + footer)

@view_config(route_name='fer')
def fer_history(request):
    header = '<h2 style="text-align: center;">Fernando Hernadez Vazquez</h2>'
    job1 = '<p style="text-align: center; font-family: verdana;">Universidad tecnologica de Tulancingo</p><p>HOLAA</p>'

    return Response(header + job1)