from . import views
from django.urls import path

urlpatterns = [
        path('', views.book_read, name='home'),
        path('create/',views.book_create,name='createbook'),
        path('retrieve/',views.book_read,name='retrievebook'),
        path('update/<int:id>/',views.book_update,name='updatebook'),
        path('delete/<int:pk>/',views.book_delete,name='deletebook'),
        path('listing/',views.listing,name='page_list'),
    ]