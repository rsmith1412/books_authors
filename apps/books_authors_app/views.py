from django.shortcuts import render, redirect
from apps.books_authors_app.models import *

# Create your views here.
def index(request):
    context = {"books": Book.objects.all()}
    return render(request, "books_authors_app/index.html", context)

def add_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["desc"]
        Book.objects.create(title=title, desc=desc)
        return redirect("/")

def show_book(request, id):
    context = {
        "book": Book.objects.get(id = id),
        "authors": Author.objects.all()
    }
    return render(request, "books_authors_app/show_book.html", context)

def add_author_to_book(request, id):
    if request.method == "POST":
        author_id = request.POST["author"]
        author = Author.objects.get(id=author_id)
        book = Book.objects.get(id=id)
        book.authors.add(author)
        return redirect("/books/" + id)

def authors(request):
    if request.method == "GET":
        context = {"authors": Author.objects.all()}
        return render(request, "books_authors_app/authors.html", context)
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        notes = request.POST["notes"]
        Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
        return redirect("/authors")

def show_author(request, id):
    context = {
        "author": Author.objects.get(id = id),
        "books": Book.objects.all()
    }
    return render(request, "books_authors_app/show_author.html", context)

def add_book_to_author(request, id):
    if request.method == "POST":
        book_id = request.POST["book"]
        book = Book.objects.get(id=book_id)
        author = Author.objects.get(id=id)
        author.books.add(book)
        return redirect("/authors/" + id)
