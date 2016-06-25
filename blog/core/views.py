from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post


def posts_list(request):
	posts = Post.published.all()
	template = 'posts.html'

	return render(request, template, {'posts': posts})


def post_details(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post, status='publicado', publish__year=year, publish__month=month, publish__day=day)
	template = 'post_details.html'

	return render(request, template, {'post': post})


# Class-based views
class PostListView(ListView):
	queryset = Post.published.all()
	context_object_name = 'posts'
	template_name = 'posts.html'