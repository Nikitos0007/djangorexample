from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.views.generic import TemplateView, ListView
from django.urls import reverse
from django.views import generic
from . import models

# Create your views here.
class CarView(ListView):
    def get_queryset(self):
        car = self.request.GET['car']
        return models.Car.objects.filter(car)
    model = models.Car
    template_name = 'car_rent/list_car.html'
    ordering = [ "reg_name" ]
    paginate_by = 10

class GarageView(ListView):
    def get_queryset(self):
        car = self.request.GET('car')
        return models.Garage.objects.filter