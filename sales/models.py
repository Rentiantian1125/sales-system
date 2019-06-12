from django.db import models


# 用户表
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30, null=False)
    create_at = models.DateTimeField()

    class Meta:
        db_table = 'user'


# 商品表
class Goods(models.Model):
    id = models.IntegerField(primary_key=True)
    price = models.IntegerField()
    num = models.IntegerField()
    create_at = models.DateTimeField()

    class Meta:
        db_table = 'goods'


# 采购订单表
class PurchaseOrder(models.Model):
    user = models.ForeignKey(User, on_delete='CASCADE')
    id = models.IntegerField(primary_key=True)
    create_at = models.DateTimeField()


# 采购表
class Purchase(models.Model):
    order = models.ForeignKey(PurchaseOrder, on_delete='CASCADE')
    id = models.IntegerField(primary_key=True)
    goods_id = models.IntegerField()
    price = models.IntegerField()
    num = models.IntegerField()
    create_at = models.DateTimeField()

    class Meta:
        db_table = 'Purchase'


# 销售订单表
class SellOrder(models.Model):
    user = models.ForeignKey(User, on_delete='CASCADE')
    id = models.IntegerField(primary_key=True)
    create_at = models.DateTimeField()


# 销售表
class Sell(models.Model):
    order = models.ForeignKey(SellOrder, on_delete='CASCADE')
    id = models.IntegerField(primary_key=True)
    goods_id = models.IntegerField()
    price = models.IntegerField()
    num = models.IntegerField()
    create_at = models.DateTimeField()

    class Meta:
        db_table = 'sell'


# 库存表
class Reserve(models.Model):
    goods = models.ForeignKey(Goods, on_delete='CASCADE')
    id = models.IntegerField(primary_key=True)
    num = models.IntegerField()
    create_at = models.DateTimeField()

    class Meta:
        db_table = 'reserve'


