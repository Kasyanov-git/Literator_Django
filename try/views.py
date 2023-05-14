from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .Textonator.final import buttonClicked
from django.views.generic import TemplateView, ListView
from .models import SearchingBooks
from django.db.models import Q
global_book_list = {}
global_recommended_books = {'b_1_ru_title': '', 'b_1_icon': '/main/static/main/img/no_book.png',
                            'b_2_ru_title': '', 'b_2_icon': '/main/static/main/img/no_book.png',
                            'b_3_ru_title': '', 'b_3_icon': '/main/static/main/img/no_book.png'}

def buttonClick(request):
    global global_recommended_books
    a = request.POST
    global_recommended_books = buttonClicked(a['book_1'], a['book_2'], a['book_3'])

    return render(request, 'try/genre.html', global_recommended_books)
# Create your views here.

def try_home(request):
    return render(request, 'try/try.html')

def try_1(request):
    return render(request, 'try/try_1.html')

def try_2(request):
    return render(request, 'try/try_2.html')

def try_3(request):
    return render(request, 'try/try_3.html')

def genre(request):
    return render(request, 'try/genre.html')

def results(request):
    global global_book_list
    global global_recommended_books
    num = 0
    book = {}
    recommended_books = {}
    book_1 = global_recommended_books['1_book']
    title_1 = book_1['b_1_en_title']
    object = SearchingBooks.objects.filter(Q(title_en=title_1))
    for i in object:
        book[f'book_1_name'] = i.icon.url

    book_2 = global_recommended_books['2_book']
    title_2 = book_2['b_2_en_title']
    object = SearchingBooks.objects.filter(Q(title_en=title_2))
    for i in object:
        book[f'book_2_name'] = i.icon.url

    book_3 = global_recommended_books['3_book']
    title_3 = book_3['b_3_en_title']
    object = SearchingBooks.objects.filter(Q(title_en=title_3))
    for i in object:
        book[f'book_3_name'] = i.icon.url

    recommended_books= {'Books_result': book}
    return render(request, 'try/results.html', recommended_books)



# def get_query(request): # новый
#     global global_num
#     global global_book_list
#     query = request.GET['q']
#     object_list = Books.objects.filter(
#         Q(title_en=query) | Q(title_ru=query)
#     )
#     for i in object_list:
#         if global_num > 3:
#             global_num = 1
#         global_book_list[f"b_{global_num}_ru_title"] = i.title_ru
#         global_book_list[f"b_{global_num}_icon"] = i.icon.url
#         global_num += 1
#
#     liked_books = {'liked_book': global_book_list}
#     print(liked_books)
#     return render(request, 'main/index.html', liked_books)

def get_query_book_1(request): # новый
    global global_book_list
    object_list1 = SearchingBooks.objects.filter(Q(title_en=request.GET['q1']) | Q(title_ru=request.GET['q1']))
    for i in object_list1:
        global_book_list[f"b_1_ru_title"] = i.title_ru
        global_book_list[f"b_1_icon"] = i.icon.url
        global_book_list[f"b_2_icon"] = '/main/static/main/img/no_book.png'
        global_book_list[f"b_3_icon"] = '/main/static/main/img/no_book.png'
    if request.GET['q1'] == '':
        global_book_list[f"b_1_ru_title"] = ''
        global_book_list[f"b_1_icon"] = '/main/static/main/img/no_book.png'
        global_book_list[f"b_2_ru_title"] = ''
        global_book_list[f"b_2_icon"] = '/main/static/main/img/no_book.png'
        global_book_list[f"b_3_ru_title"] = ''
        global_book_list[f"b_3_icon"] = '/main/static/main/img/no_book.png'
        num = 1
    else: num = 2
    liked_books = {'liked_book': global_book_list}
    print(liked_books)
    return render(request, f'try/try_{num}.html', liked_books)

def get_query_book_2(request): # новый
    global global_book_list
    object_list2 = SearchingBooks.objects.filter(Q(title_en=request.GET['q2']) | Q(title_ru=request.GET['q2']))
    for i in object_list2:
        global_book_list[f"b_2_ru_title"] = i.title_ru
        global_book_list[f"b_2_icon"] = i.icon.url
    if request.GET['q2'] == '':
        global_book_list[f"b_2_ru_title"] = ''
        global_book_list[f"b_2_icon"] = '/main/static/main/img/no_book.png'
        global_book_list[f"b_3_ru_title"] = ''
        global_book_list[f"b_3_icon"] = '/main/static/main/img/no_book.png'
        num = 1
    else: num = 3
    liked_books = {'liked_book': global_book_list}
    print(liked_books)
    return render(request, f'try/try_{num}.html', liked_books)

def get_query_book_3(request): # новый
    global global_book_list
    object_list3 = SearchingBooks.objects.filter(Q(title_en=request.GET['q3']) | Q(title_ru=request.GET['q3']))
    for i in object_list3:
        global_book_list[f"b_3_ru_title"] = i.title_ru
        global_book_list[f"b_3_icon"] = i.icon.url
    if request.GET['q3'] == '':
        global_book_list[f"b_3_ru_title"] = ''
        global_book_list[f"b_3_icon"] = '/main/static/main/img/no_book.png'
        num = 2
    else: num = 3
    liked_books = {'liked_book': global_book_list}
    print(liked_books)
    return render(request, f'try/try_{num}.html', liked_books)