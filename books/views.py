# Create your views here.
import random
from django.urls import reverse 
from django.views import generic
from .models import *

#Index View
class IndexView(generic.TemplateView): 
    template_name = 'books/index.html' 
    def get_context_data(self, **kwargs):
       context_data = super().get_context_data(**kwargs)
       context_data['recent_book1'] = Book.objects.all().order_by("-id")[0]
       context_data['recent_book2'] = Book.objects.all().order_by("-id")[1]
       context_data['top_book1'] = Book.objects.get(id=random.randint(60,69))
       context_data['top_book2'] = Book.objects.get(id=random.randint(80,89))
       return context_data
        
#Books List  Views
class BookSearchListView(generic.ListView): 
    model = Book 
    template_name = 'books/book-list.html' 
    context_object_name = 'books'
    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context_data = super().get_context_data(**kwargs)
        books=Book.objects.order_by("-isbn").filter(title__icontains=query)
        context_data['books']=books
        return context_data

class BookRecentListView(generic.ListView): 
    model = Book 
    template_name = 'books/book-list.html' 
    context_object_name = 'books'
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        books=Book.objects.all().order_by("-id")
        context_data['books']=books
        return context_data

class BookListView(generic.ListView): 
    model = Book 
    template_name = 'books/book-list.html' 
    context_object_name = 'books'
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        books=Book.objects.all().order_by("title")
        context_data['books']=books
        return context_data

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book-detail.html' 
    context_object_name = 'book'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(id=self.kwargs['pk'])
        return context
         