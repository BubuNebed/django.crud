
from django.views import generic
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class PostListViews(generic.ListView):
  model = Post
  fields= "__all__"
  success_url= reverse_lazy('blog:all')

class PostDetailViews(generic.DetailView):
  model = Post

class PostCreateViews(generic.CreateView):
  model = "__all__"
  success_url= reverse_lazy('blog:all')

class PostUpdateViews(generic.UpdateView):
  model = Post
  fields= "__all__"
  success_url= reverse_lazy('blog:all')

class PostDeleteViews(generic.DeleteView):

   model = Post
   fields= "__all__"
   success_url= reverse_lazy('blog:all')