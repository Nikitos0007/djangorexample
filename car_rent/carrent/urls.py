from django.urls import path

from . import views

app_name = 'carrent'

urlpatterns = [
    path('', views.Car.as_view(), name='car'),
    path('', views.Garage.as_view(), name='garage'),
    ##path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    ##path('<int:question_id>/vote/', views.vote, name='vote'),
]
