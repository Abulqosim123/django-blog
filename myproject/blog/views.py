from django.shortcuts import get_object_or_404,render
from .models import Post
from django.http import Http404
# Create your views her

def post_list(request):
    posts = Post.published.all()
    return render(
        request,
        'list.html',
        {'posts':posts}
    )

def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id = id,
        status = Post.Status.PUBLISHED
    )
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404('Post not found')
    return render(
        request,
        'detail.html',
        {'post':post}
    )