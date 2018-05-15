# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, routers

# Create your views here.

from zjapp.models import ProjectModel, PurchaseOrderModel, OrderProjectModel, DepartmentModel, CategoryModel, User
from zjapp.serializers import ProjectModelSerializer, PurchaseOrderModelSerializer, OrderProjectModelSerializer, \
    DepartmentModelSerializer, CategoryModelSerializer, UserSerializer

router = routers.DefaultRouter()


# 部门
class DepartmentModelViewSet(viewsets.ModelViewSet):
    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentModelSerializer


router.register('departmentmodel', DepartmentModelViewSet, base_name='departmentmodel')


# 部门类别
class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer


router.register('categorymodel', CategoryModelViewSet, base_name='categorymodel')


# 用户管理
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router.register('usermodel', UserModelViewSet, base_name='usermodel')


# 货物
class ProjectModelViewSet(viewsets.ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectModelSerializer


router.register('projectmodel', ProjectModelViewSet, base_name='projectmodel')


# 订单
class PurchaseOrderModelViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrderModel.objects.all()
    serializer_class = PurchaseOrderModelSerializer


router.register('purchaseordermodel', PurchaseOrderModelViewSet, base_name='purchaseordermodel')


# 订单货物
class OrderProjectModelViewSet(viewsets.ModelViewSet):
    queryset = OrderProjectModel.objects.all()
    serializer_class = OrderProjectModelSerializer


router.register('orderprojectmodel', PurchaseOrderModelViewSet, base_name='orderprojectmodel')
