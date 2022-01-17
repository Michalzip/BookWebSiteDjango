from django.urls import path

from . import views
urlpatterns=[

path("",views.index,name="index"),
path('book/<int:bookId>/',views.showDetailBook,name="showDetailBook")


]