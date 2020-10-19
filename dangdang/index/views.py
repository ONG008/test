from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from index.models import TClass, TBook


def index(request):
    islogin = request.session.get('is_login')
    username = request.session.get('username')
    cates1 = TClass.objects.filter(level=1)
    cates2 = TClass.objects.filter(level=2)
    cates3 = TBook.objects.order_by('-pulish_time')[:8]
    cates4 = TBook.objects.order_by('sales')[:5]
    cates5 = TBook.objects.order_by('editor_recommendatio')[:8]
    return render(request, 'index.html',
                  {'cates1': cates1, 'cates2': cates2,'cates3': cates3, 'cates4': cates4, 'cates5': cates5,
                   'islogin': islogin, 'username': username})

def booklist(request):
    islogin = request.session.get('is_login')
    username = request.session.get('username')
    class1 = request.GET.get('class1')
    class2 = request.GET.get('class2')
    num = request.GET.get('num', 1)
    if class1 and class1 != "None":
        books = TBook.objects.filter(class_field__parent_id=class1)
        request.session['calss1'] = class1
    else:
        books = TBook.objects.filter(class_field=class2)

    cates1 = TClass.objects.filter(level=1)
    cates2 = TClass.objects.filter(level=2)
    pagtor = Paginator(books, per_page=3)
    page = pagtor.page(num)
    return render(request, 'booklist.html',
                  {'cates1': cates1, 'cates2': cates2, 'books': books, 'page': page, 'class1': class1, 'class2': class2,
                   'islogin': islogin, 'username': username})


def book_detail(request):
    islogin = request.session.get('is_login')
    username = request.session.get('username')
    book_id = request.GET.get("book_id")
    if request.session.get('book_id') and book_id is None:
        book = TBook.objects.get(book_id=request.session.get('book_id'))
    else:
        request.session['book_id']=book_id
        book = TBook.objects.get(book_id=book_id)
    return render(request, 'Book details.html', {'book': book, 'islogin': islogin, 'username': username})


