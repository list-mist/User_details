from rest_framework.serializers import ModelSerializer
from .models import AddUser
from rest_framework import  serializers
class Show(serializers.ModelSerializer):

    class Meta:
        model = AddUser
        fields = ['username','email','address']  # __all__
        