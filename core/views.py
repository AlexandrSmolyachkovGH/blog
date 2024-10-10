from django.shortcuts import render, get_object_or_404

from .forms import PostSearchForm
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

class TagListView(HomeView):

    def get_template_names(self):
        return 'core/components/tag.html'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['tag'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag']
        return context

def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    related_post = Post.objects.filter(author=post.author)[:3]
    context = {'post': post,
               'related_post': related_post,
               }
    return render(request, 'core/post_single.html', context=context)

class PostSearch(HomeView):
    form_class = PostSearchForm

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return Post.objects.filter(title__icontains=form.cleaned_data['q'])
    def get_template_names(self):
        if self.request.htmx:
            return 'core/components/search_list_elements.html'
        return 'core/search.html'