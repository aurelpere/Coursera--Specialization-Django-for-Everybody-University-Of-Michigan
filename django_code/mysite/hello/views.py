from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader

def myview(request):
    print(request.COOKIES)
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('e6ca77b0  view count='+str(num_visits))
    resp.set_cookie('dj4e_cookie', 'e6ca77b0', max_age=1000)

    return resp




