from django.shortcuts import render_to_response
import datetime
from books.models import Book
from django.http import HttpResponse


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':now})

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q)>20:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'books': books, 'query':q})
    return render_to_response('search_form.html', {'error': error})
