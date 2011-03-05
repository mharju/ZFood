from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse

from utils import zfood

def store(request):
    if request.method == 'POST':
        zfood.store(request.POST['items'])
    request.session['saved'] = True 
    return HttpResponseRedirect('/')

def csv(request):
    response = HttpResponse(mimetype="text/csv")
    response['Content-Disposition'] = 'attachment; filename=zfood.csv'
    with open('zfood.csv') as f:
        response.write( f )
    return response

def index(request):
    items = zfood.read()
    saved = request.session.get('saved', False)
    if saved: del request.session['saved']
    return render_to_response('index.html', {'saved': request.session.get('saved', False), 'items': items})
