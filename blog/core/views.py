from django.shortcuts import render, get_object_or_404
from .models import Post

def posts_list(request):
	posts = Post.published.all()
	template = 'posts.html'

	return render(request, template, {'posts': posts})

def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post, status='publicado', publish__year=year, publish__month=month, publish__day=day)
	template = 'post_detail.html'

	return render(request, template, {'post': post})
