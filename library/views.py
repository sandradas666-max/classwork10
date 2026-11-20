from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'create.html', {'form': form})

def book_read(request):
    book_list=Book.objects.all()
    return render(request,'retrieve.html',{'book_list':book_list})

def book_update(request, id):
    book = Book.objects.get(pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =BookForm(instance=book)           
    return render(request, 'update.html', {'form': form})

from django.shortcuts import render
def book_delete(request,pk):
    book=Book.objects.get(pk=pk)  
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    
    return render(request,'delete.html',{'book':book})

from django.core.paginator import Paginator

def listing(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 5)  # Set the number of items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj})

# Create your views here.
