from .models import User, Author, Book
from django.http import JsonResponse
from django.shortcuts import redirect


def add_book(request):

    if request.method == 'POST':
        user = User.objects.get(pk=1)

        data = {
            'title': request.POST['title'],
            'content': request.POST['review'],
            'rating': request.POST['rating'],
        }

        # Create new author or add author
        author_name = request.POST['new_author']
        print('About to see if a new author was provided')
        if len(author_name) > 0:
            try:
                print(' Trying to get existin author')
                author = Author.objects.get(name=author_name)
            except:
                print('Trying to create a new author')
                Author.objects.create(name=author_name)
        else:
            print('About to set author to existing author')
            author_name = request.POST['author']
            author = Author.objects.get(name=author_name)
            print('Author is ', author)

        # Create book entry
        try:
            book = Book.objects.get(title=data['title'])
        except:
            book = Book.objects.create(title=data['title'], author=author)  # noqa
            book.user.add(user)
            print('New book added')

    return redirect('/books')


def view_books(request):
    books = Book.objects.all()

    output = {}
    for book in books:
        output[book.id] = book.title

    return JsonResponse(output)
