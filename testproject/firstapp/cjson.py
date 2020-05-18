from .models import Activity_Periods, Members
from rest_framework import serializers


class AccountSer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'
