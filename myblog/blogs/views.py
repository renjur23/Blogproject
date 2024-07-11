from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from .forms import BlogForm

class BlogListView(ListView):
    model = Blog
    template_name = "bloglist.html"
    context_object_name = "blogs"

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogdetail.html"
    context_object_name = "blog"

class BlogCreateView(CreateView):
    model = Blog
    template_name = "blogcreate.html"
    form_class = BlogForm
    success_url = reverse_lazy("bloglist")

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blogupdate.html"
    form_class = BlogForm

    def get_success_url(self):
        return reverse_lazy("blogdetail", kwargs={"pk": self.object.pk})

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blogdelete.html"
    success_url = reverse_lazy("bloglist")

def about(request):
    return render(request, 'about.html')
