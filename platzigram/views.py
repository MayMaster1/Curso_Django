"""platzigram views"""
from django.http import HttpResponse

#Utilities
from datetime import datetime

#Funcion de hollo_world
def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('la hora es . .{now}'.format(now=now))


def hi(request):
    """"Hi"""
    
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    #import pdb; pdb.set_trace()
    return HttpResponse(str(numbers),content_type='application/json')

    