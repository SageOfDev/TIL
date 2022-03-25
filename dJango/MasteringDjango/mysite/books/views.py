from django.shortcuts import render
from django.http import HttpResponse

from .models import Book


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append("Enter a search term.")
        elif len(q) > 20:
            errors.append("Please enter at most 20 characters")
        else:
            books = Book.objects.filter(title__icontains=q)
            context = {
                'query': q,
                'books': books,
            }
            return render(request, 'books/search_result.html', context)
    return render(request, 'books/search_form.html', {'errors': errors})
