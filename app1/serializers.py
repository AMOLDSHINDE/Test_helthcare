from rest_framework import serializers
from app1.models import Livehealths, Pationt_Register, Appointment
# from .models import *

class LivehealthsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livehealths
        fields = "__all__"

class PationRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pationt_Register
        fields = "__all__"

class AppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
