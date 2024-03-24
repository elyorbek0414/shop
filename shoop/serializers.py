from rest_framework import serializers
from .models import Mahsulot, Buyurtma, Chegirma


class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'


class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'


class chegirmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chegirma
        fields = '__all__'
