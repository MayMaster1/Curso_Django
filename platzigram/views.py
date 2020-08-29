"""platzigram views"""
from django.http import HttpResponse

#Utilities
from datetime import datetime

#Funcion de hollo_world
def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('la hora es . .{now}'.format(now=now))


def sort_integers(request):
    """"Return a JSON response with sorted integers"""
    
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    #import pdb; pdb.set_trace()
    return HttpResponse(str(numbers),content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry{}. no puedes ingresar al sitio.'.format(name)
    else:
        message = 'Hola {}. Bienvenida.'.format(name)
    return HttpResponse(message)




    