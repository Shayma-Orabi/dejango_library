from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Author, Book
from . forms import AuthorForm, BookForm


# Create your views here.
@login_required(login_url="/users/login/")
def authors_list(request):
    authors = Author.objects.all()
    return render(request,'authorlist.html',{'authors': authors})
@login_required(login_url="/users/login/")
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            newAuthoe = form.save()
            return redirect('library:list')
    else:
        form = AuthorForm()
        return render(request, 'author_update.html',{'form':form})
@login_required(login_url="/users/login/")
def edit_author(request, author_id):
    au = Author.objects.get(pk = author_id)
    form = AuthorForm(request.POST or None, instance=au)
    if form.is_valid():
        form.save()
        return redirect('library:list')
    return render(request, 'author_update.html',{'author': au,'form': form})
@login_required(login_url="/users/login/")
def delete_author(request,author_id):
    au = Author.objects.get(pk = author_id)
    au.delete()
    return redirect('library:list')
@login_required(login_url="/users/login/")
def book_list(request, author_id):
    books = Book.objects.filter(author_id=author_id)
    return render(request,'book_list.html',{'books': books, 'author_id': author_id})
@login_required(login_url="/users/login/")
def add_book(request, author_id):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            au = Author.objects.get(pk = author_id)
            newBook = form.save(commit=False)
            newBook.author = au
            newBook = form.save()
            return redirect('library:list')
    else:
        form = BookForm()
        return render(request, 'book_update.html',{'form':form, 'author_id': author_id})
@login_required(login_url="/users/login/")
def edit_book(request, book_id):
    bo = Book.objects.get(pk = book_id)
    form = BookForm(request.POST or None, instance=bo)
    if form.is_valid():
        form.save()
        return redirect('library:list')
    return render(request, 'book_update.html',{'book': bo, 'form':form, 'author_id': bo.author_id})
@login_required(login_url="/users/login/")
def delete_book(request,book_id):
    bo = Book.objects.get(pk = book_id)
    bo.delete()
    return redirect('library:list')
