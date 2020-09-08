from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'books' 
urlpatterns = [ 
    # ex: /readospher/ 
    path('', views.IndexView.as_view(), name='index'), 
    path('books/', views.BookSearchListView.as_view(), name='book-search-list'),
    path('books/top', views.BookListView.as_view(), name='book-top-list'),
    path('books/recent', views.BookRecentListView.as_view(), name='book-recent-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

