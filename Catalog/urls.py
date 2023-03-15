from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('author_list/', views.AuthorListView.as_view(),
         name='author_list'),
    path('Author_detail/<int:pk>',
         views.AuthorDetailView.as_view(), name='author_detail'),
    path('my_books/', views.LoanedBooksByUserListView.as_view(),
         name='my_books'),
    path('author/create/', views.AuthorCreateView.as_view(),
         name='author_create'),
    path('author/<int:pk>/update/',
         views.AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:pk>/delete/',
         views.AuthorDeleteView.as_view(), name='author_delete'),
    path('my_books/',
         views.LoanedBooksByUserListView.as_view(), name='my_books'),
    path('book/<uuid:pk>/loan/',
         views.loan_book_librarian, name='loan_book_librarian'),
    path('available/',
         views.AvailBooksListView.as_view(), name='all_available'),
]
