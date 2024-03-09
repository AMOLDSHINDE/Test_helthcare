from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Livehealths, Pationt_Register,Appointment
from .serializers import LivehealthsSerializers, PationRegisterSerializers,AppointmentSerializers
from rest_framework import viewsets
# Create your views here.

class Register(viewsets.ModelViewSet):
    queryset =  Livehealths.objects.all()
    serializer_class = LivehealthsSerializers

class Pation_Resgister(viewsets.ModelViewSet):
    queryset = Pationt_Register.objects.all()
    serializer_class = PationRegisterSerializers

class Appointments(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers


