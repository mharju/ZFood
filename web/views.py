from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.conf import settings

from utils import zfood

def store(request):
    if request.method == 'POST':
        try:
            zfood.store(request.POST['items'], filename=settings.CSV_LOCATION)
        except Exception, e:
            request.session['error'] = e
    request.session['saved'] = True 
    return HttpResponseRedirect('/zfood/')

def csv(request):
    response = HttpResponse(mimetype="text/csv")
    response['Content-Disposition'] = 'attachment; filename=zfood.csv'
    with open(settings.CSV_LOCATION) as f:
        response.write( f )
    return response

def index(request):
    items = zfood.read(filename=settings.CSV_LOCATION)
    saved = request.session.get('saved', False)
    if saved: del request.session['saved']
    return render_to_response('index.html', {'saved': request.session.get('saved', False), 'items': items})
