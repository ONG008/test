from datetime import date, time, datetime
import time
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from car.car import Car
from car.models import ShoppingCart
from order.models import TAddress, TOrder, OrderItem
from user.models import TUser


def indent(request):
    username = request.session.get('username')
    user_id = TUser.objects.get(username=username).id
    books = ShoppingCart.objects.filter(user=user_id)
    addresss = TAddress.objects.filter(user_id=user_id)
    car = Car()
    for book in books:
        id = book.book_id
        count = book.book_num
        car.add_book(id, count)
    total = 0
    for i in car.book_list:
        total += float(i.price) * int(i.count)
    return render(request, 'indent.html', {'car': car.book_list, 'username': username,
                                           'total': round(total, 2), 'addresss': addresss})


def indent_ok(request):
    order_id = int(request.GET.get('order_id'))
    total = request.GET.get('total')
    # number = request.GET.get('number')
    number = 0
    username = request.session.get('username')
    # 从地址表中查出收件人姓名
    address_id = TOrder.objects.filter(order_id=order_id)[0].address_id
    print(address_id)
    name = TAddress.objects.filter(id=address_id)[0].name
    # 从订单项表中查询商品数量
    books = OrderItem.objects.filter(order_id=order_id)
    for book in books:
        number += book.count
    return render(request, 'indent ok.html', {'username': username, 'order_id': order_id, 'total': total,
                                              'number': number, 'name': name})


def address(request):
    consignee_name = request.POST.get('consignee_name')
    detail_address = request.POST.get('detail_address')
    post_code = request.POST.get('post_code')
    cellphone = request.POST.get('cellphone')
    telephone = request.POST.get('telephone')
    username = request.session.get('username')
    user_id = TUser.objects.filter(username=username)[0].id
    # 创建订单对象
    books = ShoppingCart.objects.filter(user=user_id)
    car = Car()
    for book in books:
        id = book.book_id
        count = book.book_num
        number = 0
        number += count
        car.add_book(id, count)
    total = 0
    for i in car.book_list:
        total += float(i.price) * float(i.count)
    # 判断收货地址表是否已有该用户的收货地址,获取
    if TAddress.objects.filter(user_id=user_id, name=consignee_name, detail_address=detail_address):
        address_id = TAddress.objects.filter(user_id=user_id, name=consignee_name, detail_address=detail_address)[0].id
        create_time = datetime.now()
        order_id = int(str(time.strftime('%m%d%H%M%S', time.localtime(time.time()))))
        TOrder.objects.create(
            order_id=order_id,
            all_price=total,
            create_time=create_time,
            address_id=address_id,
            user_id=user_id,
        )
        for book in car.book_list:
            print(order_id, type(order_id))
            OrderItem.objects.create(
                order_id=order_id,
                count=int(book.count),
                book_id=book.id,
            )
        return JsonResponse({'order_id': order_id, 'username': username, 'total': total,
                             'number': number})
    # 没有收货地址，添加收货地址
    else:
        TAddress.objects.create(
            name=consignee_name,
            detail_address=detail_address,
            post_code=post_code,
            cellphone=cellphone,
            telephone=telephone,
            user_id=user_id,
        )
        address_id = TAddress.objects.filter(user_id=user_id, name=consignee_name, detail_address=detail_address)[0].id
        create_time = datetime.now()
        order_id = int(str(time.strftime('%m%d%H%M%S', time.localtime(time.time()))))
        TOrder.objects.create(
            order_id=order_id,
            all_price=total,
            create_time=create_time,
            address_id=address_id,
            user_id=user_id,
        )
        for book in car.book_list:
            OrderItem.objects.create(
                order_id=order_id,
                count=int(book.count),
                book_id=int(book.id),
            )
        return JsonResponse({'order_id': order_id, 'username': username, 'total': total,
                             'number': number,})