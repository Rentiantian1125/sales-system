from django.db import models
from django.utils import timezone


# 用户表
class User(models.Model):
    id = models.AutoField(primary_key=True)
    # id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30, null=False)
    create_at = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = 'user'


# 商品表
class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, default='')
    # id = models.IntegerField(primary_key=True)
    price = models.IntegerField()
    create_at = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = 'goods'


# 采购订单表
class PurchaseOrder(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete='CASCADE')
    # id = models.IntegerField(primary_key=True)
    create_at = models.DateTimeField(default=timezone.now())
    status = models.IntegerField()


# 采购表
class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(PurchaseOrder, on_delete='CASCADE')
    # id = models.IntegerField(primary_key=True)
    goods_id = models.IntegerField()
    price = models.IntegerField()
    num = models.IntegerField()
    create_at = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = 'Purchase'


# 销售订单表
class SellOrder(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete='CASCADE')
    # id = models.IntegerField(primary_key=True)
    create_at = models.DateTimeField(default=timezone.now())
    status = models.IntegerField()


# 销售表
class Sell(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(SellOrder, on_delete='CASCADE')
    # id = models.IntegerField(primary_key=True)
    goods_id = models.IntegerField()
    price = models.IntegerField()
    num = models.IntegerField()
    create_at = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = 'sell'


# 库存表
class Reserve(models.Model):
    id = models.AutoField(primary_key=True)
    goods = models.ForeignKey(Goods, on_delete='CASCADE')
    # id = models.IntegerField(primary_key=True)
    num = models.IntegerField()
    create_at = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = 'reserve'
