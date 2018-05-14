# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, routers

# Create your views here.

router = routers.DefaultRouter()

# 货物
from zjapp.models import ProjectModel, PurchaseOrderModel, OrderProjectModel
from zjapp.serializers import ProjectModelSerializer, PurchaseOrderModelSerializer, OrderProjectModelSerializer


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
