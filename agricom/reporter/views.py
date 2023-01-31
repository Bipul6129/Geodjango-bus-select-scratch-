from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse,JsonResponse
from .models import Incidences,Bus
import json
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'landing/index.html'

def incidence(request):
    inciden = serialize('geojson',Incidences.objects.all())
    print("worked")
    return HttpResponse(inciden,content_type='json')

class TrialPageView(TemplateView):
    template_name = 'landing/trial.html'


def get_markers(request,safe=True):
    inciden =serialize('geojson',Incidences.objects.all())
    print("worked")
    # count=0
    # for obj in inciden:
    #     count+1
    #     print(obj.location.x)
    #     data = {'markerid':count,'lat':obj.location.x,'lon':obj.location.y}

    # data = [model_instance.as_dict() for model_instance in inciden]
    # print(len(data))
    return HttpResponse(inciden,content_type='json')

def bus_markers(request,yatayat):
    markers = serialize('geojson',Bus.objects.filter(yatayat=yatayat))
    return HttpResponse(markers,content_type='json')

class BusMarkerPage(TemplateView):
    template_name = 'landing/bus.html'

# def busmarkerpage(request,yatayat):
#     return render(request,'landing/bus.html')