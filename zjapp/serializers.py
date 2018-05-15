# coding:utf-8
from rest_framework import serializers

from zjapp.models import ProjectModel, PurchaseOrderModel, OrderProjectModel, DepartmentModel, CategoryModel, User


class DepartmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentModel
        fields = '__all__'


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'


class PurchaseOrderModelSerializer(serializers.ModelSerializer):
    # products =
    class Meta:
        model = PurchaseOrderModel
        fields = '__all__'


class OrderProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProjectModel
        fields = '__all__'
