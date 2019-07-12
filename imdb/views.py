# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render , render_to_response
from django.http import HttpResponse
from .models import imdb

# Create your views here.
def index(request):
    return render(request,'index.html',{})


#from django.utils import simplejson
#def autocompleteModel(request):
#    search_qs = ModelName.objects.filter(name__startswith=request.REQUEST['search'])
#    results = []
#    for r in search_qs:
#        results.append(r.name)
#    resp = request.REQUEST['callback'] + '(' + simplejson.dumps(result) + ');'
#    return HttpResponse(resp, content_type='application/json')

def search_titles(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    #print(imdb.objects.all())
    data = imdb.objects.order_by('raing').filter(moviename__icontains=str(search_text))[:5]
    print(data)

    articles = data
    return render_to_response('search_script.html',{'articles':articles})

def result(request,num=0):
    data = imdb.objects.get(id=num)
    return render(request,'results.html',{'data':data})