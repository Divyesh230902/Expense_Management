from rest_framework import serializers
from .models import Basket, Dashboard

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"

class DatesSerializer(serializers.Serializer):
    date = serializers.DateField()
    count = serializers.IntegerField()

class DasboardSerializer(serializers.ModelSerializer):
    savings = serializers.SerializerMethodField()
    class Meta:
        model = Dashboard
        fields = "__all__"
    
    def get_savings(self,obj):
        return obj.user.userdata.daily_saving