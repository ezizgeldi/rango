from django.core import paginator
from django.shortcuts import render,  get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'blog/index.html', context)


# def post_list(request):
#     object_list = Post.objects.all()
#     paginator = Paginator(object_list, 3)  # from 3 page
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     context = {
#         'posts': posts,
#         'page': page
#     }
#     return render(request, 'blog/post/list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,  status='published',
                             publish__year=year, publish__month=month, publish__day=day)
    context = {'post': post}
    return render(request, 'blog/post/detail.html', context)
