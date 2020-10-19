import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from car.car import Car, Book
from car.models import ShoppingCart
from index.models import TBook
from order.models import TAddress
from user.models import TUser


def mydefault(book):
    if isinstance(book, Book):
        return {'id': book.id, 'title': book.title,
                'count': book.count, 'price': book.price,
                'picture': book.pictrue}


def car(request):

    islogin = request.session.get('is_login')
    # 判断是否登录，已登录从数据库中获取购物车数据渲染页面
    if islogin:
        # 判断购物车表中是否有该用户的购物车,如果有则获取数据

        username = request.session.get('username')
        user_id = TUser.objects.get(username=username).id
        books = ShoppingCart.objects.filter(user=user_id)
        addresss = TAddress.objects.filter(user_id=user_id)
        if books:
            # 从购车表中拿出这个人的购物车的书和数量构建前端购物车car对象
            car = Car()
            for book in books:
                id = book.book_id
                count = book.book_num
                car.add_book(id, count)
            # 计算每本书的总计
            total = 0
            for i in car.book_list:
                total += float(i.price) * int(i.count)
            return render(request, 'car.html', {'car': car.book_list, 'total': round(total, 2),
                                                'islogin': islogin, 'username': username, 'addresss': addresss})
        # 如果没有购物车，则返回空购物车
        else:
            return render(request, 'car.html', {'islogin': islogin, 'username': username, 'addresss': addresss})
    # 未登录状态，从session中获取购物车数据
    else:
        car = request.session.get('car')
        username = request.session.get('username')
        # 如果已有购物车，返回购物车页面、购物车数据、小计、
        if car:
            json.dumps(list(car.book_list), default=mydefault)
            total = 0
            for i in car.book_list:
                total += (float(i.price)*int(i.count))
            return render(request, 'car.html', {'car': car.book_list, 'total': round(total, 2),
                                                'islogin': islogin, 'username': username})
        # 若没有购物车则返回空购车
        else:
            return render(request, 'car.html', {'islogin': islogin, 'username': username})


def add_car(request):

    id = request.GET.get('id')
    count = int(request.GET.get('count'))
    # 判断是否登录,已登录存入数据库
    if request.session.get('is_login'):
        # 判断是已存在这本书，直接修改数量
        username = request.session.get('username')
        user_id = TUser.objects.get(username=username).id
        books = ShoppingCart.objects.filter(user=user_id, book=id)
        if books:
            books[0].book_num = books[0].book_num + count
            books[0].save()
        # 判断否则，创建一行数据
        else:
            username = request.session.get('username')
            user_id = TUser.objects.get(username=username).id
            ShoppingCart.objects.create(
                book_id=id,
                book_num=count,
                user_id=user_id,
            )
        # 购物车里点加减号所需的总价和数量
        # car = Car()
        price = TBook.objects.filter(book_id=id)[0].discount_price
        count = ShoppingCart.objects.get(book_id=id).book_num
        total = price * count
        return JsonResponse({"total": total, 'count': count})
    # 未登录状态，存入session
    else:
        # 如果有购物车
        car = request.session.get('car')
        if car:
            pass
        else:
            car = Car()
        car.add_book(id, count)
        request.session['car'] = car
        total = 0
        for i in car.book_list:
            total += float(i.price) * int(i.count)
            if i.id==id:
                count = i.count
        return JsonResponse({"total": total, 'count': count})


def del_car(request):
    id = request.GET.get('id')
    islogin = request.session.get('is_login')
    # 判断是否是登陆状态，若已登录
    if islogin:
        username = request.session.get('username')
        user_id = TUser.objects.get(username=username).id

        # 从购物车表删除该用户的该id书的数据
        ShoppingCart.objects.filter(user=user_id, book=id)[0].delete()
        # 拿出这个用户的购物车，创建页面显示购物车对象car
        books = ShoppingCart.objects.filter(user=user_id)
        car = Car()
        for book in books:
            book_id = book.book_id
            count = book.book_num
            car.add_book(book_id, count)
        # 利用页面显示购物车对象car,计算总价total
        total = 0
        for i in car.book_list:
            total += (float(i.price) * int(i.count))
        return JsonResponse({"total": total})
    # 未登录：则从session中获取购物车>删除指定id的书
    else:
        # 从session中获取购物车
        car = request.session.get('car')
        # 删除购物车中指定书id的数据
        car.remove_book(id)
        request.session['car'] = car
        # 计算总价
        total = 0
        for i in car.book_list:
            total += (float(i.price) * int(i.count))
        return JsonResponse({"total": total})
