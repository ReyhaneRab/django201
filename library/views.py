from django.shortcuts import render, redirect, get_object_or_404
from library.models import Book
from library.forms import BookForm


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    count = book.author.author_book.count()
    return render(request, 'book_detail.html', {'book': book,
                                                'number_of_book': count})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    return render(request, 'add_book.html', {'form': BookForm()})


def edit_book(request, pk):
    obj = get_object_or_404(Book, id=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('books')
    return render(request, 'add_book.html', {'form': BookForm(instance=obj)})

