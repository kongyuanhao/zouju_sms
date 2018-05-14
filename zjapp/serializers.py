# coding:utf-8
from rest_framework import serializers

from zjapp.models import ProjectModel, PurchaseOrderModel, OrderProjectModel


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'


class PurchaseOrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderModel
        fields = '__all__'


class OrderProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProjectModel
        fields = '__all__'
