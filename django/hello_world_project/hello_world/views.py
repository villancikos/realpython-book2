from django.template import Context, loader
from datetime import datetime
from django.http import HttpResponse

def index(request):
    '''parameter request is an object with
    information about the request from the user que triggerio la view
    (that triggered the view)'''
    return HttpResponse('<html><body>Hello, World!</body></html>')


def about(request):
    return HttpResponse('Here is the About Page. Want to return home? <a href="/">Back Home</a>')

def better(request):
    t = loader.get_template('betterhello.html')
    c = Context({'current_time' : datetime.now(),})
    return HttpResponse(t.render(c))