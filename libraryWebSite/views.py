from logging import exception
from multiprocessing import context
from django.http import Http404
from django.http  import HttpResponse
from .models import Book
from django.template import loader
from django.shortcuts import render


def index(request): 
    bookSortByPrice=Book.objects.order_by('id')
    template=loader.get_template("index.html")
    contexOfPage={
        "listofBook":bookSortByPrice,
    }
    return HttpResponse(template.render(contexOfPage,request))


def showDetailBook(request, bookId):
    try:
       
        question=Book.objects.get(pk=bookId)
        context={
            'detailOfBook':question
        }
       
    except Book.DoesNotExist: 
        raise Http404("book does not exists")
    return render(request,"detailBook.html" ,context=context)




