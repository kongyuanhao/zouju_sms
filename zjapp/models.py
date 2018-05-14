# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username, password and email are required. Other fields are optional.
    """
    pass


# Create your models here.
# 产品管理/                                      02-Apr-2018 11:19                   -
# 供应商/                                         02-Apr-2018 11:20                   -
# 客户管理模块/                                02-Apr-2018 11:20                   -
# 库存模块/                                      02-Apr-2018 11:21                   -
# 财务管理模块/                                02-Apr-2018 11:21                   -
# 销售管理模块/

class ProjectModel(models.Model):
    '''
    产品管理
        产品编码
        品牌名称
        产品名称
        图片
        卖方建议零售价
        采购单价
        数量
        编辑
    '''
    number = models.CharField(help_text=u"产品编码", max_length=255, null=True, blank=True)
    brand_name = models.CharField(help_text=u"品牌名称", max_length=255, null=True, blank=True)
    name = models.CharField(help_text=u"产品名称", max_length=255, null=True, blank=True)
    images = models.CharField(help_text=u"图片", max_length=255, null=True, blank=True)


class PurchaseOrderModel(models.Model):
    '''
    进货单
        订单号
        产品
        全额预付货物数
        全额预付日期
        全额预付金额
        预付比例
        预付金额
        预付日期
        货物数量
        尾款金额
        尾款日期
        总货值
        备注
        编辑
    '''
    number = models.CharField(help_text=u"订单号", max_length=255, null=True, blank=True)
    all_pre_pay_count = models.IntegerField(help_text=u"全额预付货物数", default=0)
    all_pre_pay_date = models.DateField(help_text=u"全额预付日期", null=True, blank=True)
    all_pre_pay_money = models.FloatField(help_text=u"全额预付金额", null=True, blank=True)
    pre_pay_ratio = models.FloatField(help_text=u"预付比例", default=0.00)
    pre_pay_date = models.DateField(help_text=u"预付日期", null=True, blank=True)
    pre_pay_money = models.FloatField(help_text=u"预付金额", null=True, blank=True)
    count = models.IntegerField(help_text=u"货物数量", default=0)
    balance_pay_money = models.FloatField(help_text=u"尾款金额", default=0.00)
    balance_pay_date = models.DateField(help_text=u"尾款日期", null=True, blank=True)
    all_mongey = models.FloatField(help_text=u"总货值", default=0.00)
    mark = models.TextField(help_text=u"备注", null=True, blank=True)
    create_time = models.DateTimeField(help_text=u"创建日期", auto_now_add=True)


class OrderProjectModel(models.Model):
    '''
    订单
    产品
    卖方建议零售价
    采购单价
    数量

    '''
    order = models.ForeignKey(PurchaseOrderModel, help_text="订单", related_name='order_project')
    project = models.ForeignKey(ProjectModel, help_text="产品", related_name='project_order')
    count = models.IntegerField(help_text=u"数量", default=0)
    suggest_price = models.FloatField(help_text=u"卖方建议零售价", default=0.00)
    purchase_price = models.FloatField(help_text=u"采购单价", default=0.00)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.order.count += self.count
        self.order.all_mongey += self.count * self.purchase_price


class SupplierModel(models.Model):
    '''
    供应商
    '''


class CustomerModel(models.Model):
    '''
    客户管理模块
    '''


class StockrModel(models.Model):
    '''
    库存模块
    '''


class FinanceModel(models.Model):
    '''
    财务管理模块
    '''


class MarketModel(models.Model):
    '''
    销售管理模块
    '''
