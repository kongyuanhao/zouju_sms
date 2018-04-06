# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


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
        订单号
        订单数量
        卖方建议零售价
        采购单价
        全额预付货物数
        全额预付款日期
        全额预付金额
        预付比例
        预付金额
        预付日期
        货物数量
        尾款金额
        尾款日期
        总货值
    '''


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
