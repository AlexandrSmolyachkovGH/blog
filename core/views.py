from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView


# Create your views here.
class HomeView(ListView):
    model = Post
    # template_name = 'core/index.html'
    context_object_name = 'posts'
    paginate_by = 10  # display posts on page

    def get_template_names(self):
        if self.request.htmx:
            return 'core/components/post_list_elements.html'
        return 'core/index.html'


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    related_post = Post.objects.filter(author=post.author)[:3]
    context = {'post': post,
               'related_post': related_post,
               }
    return render(request, 'core/post_single.html', context=context)
