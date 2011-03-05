from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from utils import zfood

import os.path

def _csv_filename(user):
    return os.path.join(settings.CSV_LOCATION, '%s.csv' % user.username)

def login(request):
    error = ''
    if request.method == 'POST': 
        print "%s and %s" % (request.POST['username'], request.POST['password'],)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            auth_login(request, user)
            return HttpResponseRedirect('/')
        error = 'oh noes.'

    return render_to_response('login.html', {'error': error})

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')


@login_required
def store(request):
    if request.method == 'POST':
        filename = _csv_filename(request.user)
        try:
            zfood.store(request.POST['items'], filename=filename)
        except Exception, e:
            request.session['error'] = e
    request.session['saved'] = True 
    return HttpResponseRedirect('/')

@login_required
def remove(request, id):
    filename = _csv_filename(request.user)

    zfood.remove(int(id), filename=filename)
    return HttpResponseRedirect('/')

@login_required
def csv(request):
    response = HttpResponse(mimetype="text/csv")
    response['Content-Disposition'] = 'attachment; filename=zfood.csv'
    filename = _csv_filename(request.user)
    with open(filename) as f:
        response.write( f )
    return response

@login_required
def index(request):
    filename = _csv_filename(request.user)

    items = zfood.read(filename=filename)
    saved = request.session.get('saved', False)
    if saved: del request.session['saved']
    return render_to_response('index.html', {'saved': request.session.get('saved', False), 'error': request.session.get('error', ''), 'items': items})
