from logging import exception
from multiprocessing import context
from django.http import Http404
from django.http  import HttpResponse
from .models import Book
from django.template import loader
from django.shortcuts import render


def index(request): #request musi bbyc bo do oznacza ze chcmey zadanie http
    bookSortByPrice=Book.objects.order_by('id')
    template=loader.get_template("index.html")
    contexOfPage={
        "listofBook":bookSortByPrice,
    }
    return HttpResponse(template.render(contexOfPage,request))


def showDetailBook(request, bookId):
    try:
        #wez wszytskie dane ksiazk i o podanym id
        question=Book.objects.get(pk=bookId)
        context={
            'detailOfBook':question
        }
       
    except Book.DoesNotExist: 
        raise Http404("book does not exists")
        #context=context robimy tak gdy chcemy wsiazc np dane 
        #jeszcze autora to wtedy musimy miec wiecej odniesien niz do jeden tabeli
    return render(request,"detailBook.html" ,context=context)




