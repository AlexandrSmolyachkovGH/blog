from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'core/index.html'
    context_object_name = 'posts'