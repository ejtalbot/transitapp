from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from . import allstations, getmetro, lines
from .models import Line, Station
from django.template.context_processors import csrf
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from .forms import LineForm, LineChoices

def home(request):
    return render(request, 'transit/home.html')

def findConnections(request):
    if request.GET.items():
        form = LineChoices(request.GET)
        if form.is_valid():
            current_line_dict = request.GET
            for i in current_line_dict.values():
                current_line = i
            args = { }
            args['form'] = form
            args['current_line'] = current_line
            station_list = allstations.getAllStations(current_line)['Stations']
            args['station_list'] = station_list
            return render(request, 'transit/lineConnections.html', args)
    form = LineChoices()
    args = { }
    args['form'] = form
    return render(request, 'transit/lineConnections.html', args)