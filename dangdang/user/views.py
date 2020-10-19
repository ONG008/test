import os
import random
import string

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from user.captcha.image import ImageCaptcha
from user.models import TUser


def login(request):
    url = request.GET.get('url')
    print(url)
    username = request.COOKIES.get("username")
    password = request.COOKIES.get("password")
    if TUser.objects.filter(username=username, password=password):
        # request.session['is_login'] = True
        # return redirect('index:index')
        return render(request, 'login.html', {"useranme": username, "password": password, 'url': url})
    return render(request, 'login.html', {'url': url})


def login_logic(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    if TUser.objects.filter(username=username, password=password):
        checked = request.POST.get('remember')
        request.session['is_login'] = True
        request.session['username'] = username
        homepage = HttpResponse('ok')
        if checked:
            homepage.set_cookie('username', username, max_age=7 * 24 * 3600)
            homepage.set_cookie('password', password, max_age=7 * 24 * 3600)
        return homepage
    else:
        return HttpResponse('no')


def logout(request):
    url = request.GET.get('url')
    # 修改登陆状态为未登录
    request.session['is_login'] = False
    # 删除用户名和密码的cookie
    res = JsonResponse({'islogin': False, 'url': url})
    res.set_cookie('username', max_age=0)
    res.set_cookie('password', max_age=0)
    return res


def checkusername(request):
    username = request.GET.get('username')
    res = TUser.objects.filter(username=username)
    if res:
        return HttpResponse('ok')
    else:
        return HttpResponse('no')

def register(request):
    return render(request, 'register.html')


def register_logic(request):
    username = request.POST.get('username')
    pwd = request.POST.get('password')
    user1 = TUser.objects.filter(username=username)
    if user1:
        return HttpResponse('repeat')
    else:
        TUser.objects.create(
            username=username,
            password=pwd
        )
        return HttpResponse('ok')


def checkregister(request):
    username = request.GET.get('username')
    user1 = TUser.objects.filter(username=username)
    if user1:
        return HttpResponse('repeat')
    else:
        return HttpResponse('ok')


def registerok(request):
    username = request.GET.get('username')
    return render(request, "registerok.html", {'username': username})


def getcaptcha(request):
    image = ImageCaptcha(fonts=[os.path.abspath("xxx/segoesc.ttf")])
    code = random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 4)
    random_code = "".join(code)
    request.session['code'] = random_code
    data = image.generate(random_code)

    return HttpResponse(data, "image/png")


def checkcaptcha(request):
    # print('hhhhhhh')
    code = request.session.get('code')

    print('验证码为', request.session.get('code'))
    if code.lower() == request.GET.get('code').lower():

        return HttpResponse('ok')
    else:

        return HttpResponse('no')
