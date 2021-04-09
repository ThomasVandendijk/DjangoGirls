from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post


class PostListView(ListView):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post


class PostFullView(DetailView):
    model = Post
    template_name = "blog/post_full.html"


class PostListAlternativeView(ListView):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context_object_name = 'posts'
    template_name = "blog/post_list_alternative.html"
