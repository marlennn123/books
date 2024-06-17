from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Author, Book
from .forms import BookForm

class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    queryset = Book.objects.all()
    template_name = 'book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    form_class = BookForm
    template_name = 'book_create.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    queryset = Book.objects.all()
    form_class = BookForm
    template_name = 'book_update.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    queryset = Book.objects.all()
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_list')