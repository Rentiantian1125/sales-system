from django.http import JsonResponse
from .models import *
from sales import models
from sales_system.token_service import TokenService


def auth(func):
    def view(request):
        user_info = {'id': 1, 'name': 'rentiantian'}
        return func(request, user_info)

        # token = TokenService.get_token(request)
        # if token:
        #     user_info = TokenService.check_token(token)
        # else:
        #     return JsonResponse({'code': '1', 'error_msg': '需要登录'})
        # return func(request, user_info)

    return view


def sign_in(request):
    # 登陆
    name = request.POST.get('username')
    pwd = request.POST.get('password')

    if name and pwd:
        user_obj = models.User.objects.filter(username=name, password=pwd).first()

        if user_obj:
            return JsonResponse({'code': '0', 'msg': '登录成功',
                                 'token': TokenService.create_token({'id': user_obj.id, 'name': user_obj.username})})
        else:
            return JsonResponse({'code': '1', 'msg': '用户名或密码错误'})
    else:
        return JsonResponse({'code': '1', 'msg': '输入为空'})


@auth
def add_user(request, user_info):
    # 新增用户
    name = request.POST.get('username')
    pwd = request.POST.get('password')
    if name and pwd:

        user_obj = models.User.objects.create(username=name, password=pwd)
        return JsonResponse({'code': '0', 'msg': '添加成功'}) if user_obj else JsonResponse({'code': '1', 'msg': '添加用户失败'})

    else:
        return JsonResponse({'code': '1', 'msg': '输入为空'})


@auth
def get_user_list(request, user_info):
    # 获取用户列表
    name = request.POST.get('username')

    user_list = models.User.objects.filter(username=name) if name else models.User.objects.all()

    return JsonResponse({'code': '0', 'msg': '加载成功', 'data': list(user_list)}) \
        if len(user_list) > 0 else JsonResponse({'code': '1', 'msg': '无数据'})


@auth
def get_purchase_list(request, user_info):
    # 获取采购列表
    goods_id = request.POST.get('goods_id')
    if goods_id:
        purchase_list = models.PurchaseOrder.objects.filter(goods_id=goods_id)
    else:
        purchase_list = models.PurchaseOrder.objects.all()
    if len(purchase_list) > 0:
        return JsonResponse({'code': '0', 'msg': '加载成功', 'data': list(purchase_list)})
    else:
        return JsonResponse({'code': '1', 'msg': '无数据'})


@auth
def add_purchase(request, user_info):
    # 新增采购订单
    user = request.POST.get('user')
    purchase = models.PurchaseOrder.objects.create(user=user)
    order = purchase.order
    goods_id = request.POST.get('goods_id')
    price = request.POST.get('price')
    num = request.POST.get('num')
    if order and goods_id and price and num:
        purchase_obj = models.Purchase.objects.create(id=id, order_id=order.id, goods_id=goods_id, price=price,
                                                      num=num)
        if purchase_obj:
            return JsonResponse({'code': '0', 'msg': '添加成功'})
        else:
            return JsonResponse({'code': '1', 'msg': '添加采购单失败'})
    else:
        return JsonResponse({'code': '1', 'msg': '不可为空'})


@auth
def update_purchase(request, user_info):
    # 编辑采购单
    order = request.POST.get('order')
    goods_id = request.POST.get('goods_id')
    price = request.POST.get('price')
    num = request.POST.get('num')
    if order and goods_id and price and num:
        user_obj = models.Purchase.objects.filter(id=id).update(id=id, order=order, goods_id=goods_id, price=price,
                                                                num=num)
        if user_obj:
            return JsonResponse({'code': '0', 'msg': '保存成功'})
        else:
            return JsonResponse({'code': '1', 'msg': '保存失败'})
    else:
        return JsonResponse({'code': '1', 'msg': '不可为空'})


@auth
def get_sell_list(request, user_info):
    # 获取销售列表
    goods_id = request.POST.get('goods_id')
    if goods_id:
        sell_list = models.SellOrder.objects.filter(goods_id=goods_id)
    else:
        sell_list = models.SellOrder.objects.all()
    if len(sell_list) > 0:
        return JsonResponse({'code': '0', 'msg': '加载成功', 'data': list(sell_list)})
    else:
        return JsonResponse({'code': '1', 'msg': '无数据'})


@auth
def add_sell(request, user_info):
    # 新增销售订单
    user = request.POST.get('user')
    sell = models.SellOrder.objects.create(user=user)
    order = sell.order
    goods_id = request.POST.get('goods_id')
    price = request.POST.get('price')
    num = request.POST.get('num')
    if order and goods_id and price and num:
        user_obj = models.Sell.objects.create(id=id, order_id=order, goods_id=goods_id, price=price,
                                              num=num)
        if user_obj:
            return JsonResponse({'code': '0', 'msg': '添加成功'})
        else:
            return JsonResponse({'code': '1', 'msg': '添加失败'})
    else:
        return JsonResponse({'code': '1', 'msg': '不可为空'})


@auth
def update_sell(request, user_info):
    # 编辑销售单
    order = request.POST.get('order')
    goods_id = request.POST.get('goods_id')
    price = request.POST.get('price')
    num = request.POST.get('num')
    if order and goods_id and price and num:
        user_obj = models.Sell.objects.filter(id=id).update(id=id, order=order, goods_id=goods_id, price=price,
                                                            num=num)
        if user_obj:
            return JsonResponse({'code': '0', 'msg': '添加成功'})
        else:
            return JsonResponse({'code': '1', 'msg': '添加失败'})
    else:
        return JsonResponse({'code': '1', 'msg': '不可为空'})


@auth
def get_reserve(request, user_info):
    # 获取库存信息
    goods = request.POST.get('goods')
    if goods:
        models.User.objects.filter(goods=goods)
    else:
        models.User.objects.all()


@auth
def get_goods_list(request, user_info):
    # 获取商品列表
    goods_list = Goods.objects.values().filter()

    return JsonResponse({'code': '0', 'msg': '加载成功', 'data': list(goods_list)})

    # if len(goods_list) > 0:
    #     return JsonResponse({'code': '0', 'msg': '加载成功', 'data': list(goods_list)})
    # else:
    #     return JsonResponse({'code': '1', 'msg': ''})


@auth
def add_update_goods(request, user_info):
    # 新增或编辑商品
    goods_id = request.POST.get('id', None)
    name = request.POST.get('name')
    price = request.POST.get('price')
    if name and price:
        if goods_id:
            user_obj = models.Goods.objects.filter(id=goods_id).update(name=name, price=price)
        else:
            user_obj = models.Goods.objects.create(name=name, price=price)

        if user_obj:
            return JsonResponse({'code': '0', 'msg': '添加成功'})
        else:
            return JsonResponse({'code': '1', 'msg': '添加失败'})
    else:
        return JsonResponse({'code': '1', 'msg': '不可为空'})


@auth
def update_goods(request, user_info):
    # 编辑商品
    goods_id = request.POST.get('id')
    name = request.POST.get('name')
    price = request.POST.get('price')
    if id and name and price:
        # user_obj = models.Goods.objects.create_or_update(name=name, good=good_id, price=price,
        user_obj = models.Goods.objects.filter(id=goods_id).update(name=name, price=price)

        if user_obj:
            return JsonResponse({'code': '0', 'msg': '添加成功'})
        else:
            return JsonResponse({'code': '1', 'msg': '添加失败'})
    else:
        return JsonResponse({'code': '1', 'msg': '不可为空'})


@auth
def change_goods_price(request, user_info):
    # 调价
    goods_id = request.POST.get('id')
    price = request.POST.get('price')
    if price:
        user_obj = models.Sell.objects.filter(id=goods_id).update(price=price)
        if user_obj:
            return JsonResponse({'code': '0', 'msg': '保存成功'})
        else:
            return JsonResponse({'code': '1', 'msg': '保存失败'})
    else:
        return JsonResponse({'code': '1', 'msg': '不可为空'})


@auth
def put_in_reserve(request, user_info):
    # 入库
    purchase_id = request.POST.get('id')
    goods_info = models.Purchase.objects.get(id=purchase_id)
    goods = goods_info.goods_id
    num = goods_info.num
    if goods and num:
        reserve = models.Reserve.objects.get(goods=goods)
        reserve.updata(num=int(num) + int(reserve.num))


@auth
def out_reserve(request, user_info):
    # 出库
    sell_id = request.POST.get('id')
    goods_info = models.Sell.objects.get(id=sell_id)
    goods = goods_info.goods_id
    num = goods_info.num
    if goods and num:
        reserve = models.Reserve.objects.get(goods=goods)
        reserve.updata(num=int(reserve.num) - int(num))
