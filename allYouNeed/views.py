from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'allYouNeed/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'allYouNeed/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def food(request):
    return render(request, 'allYouNeed/food.html', {'title': 'Food'})


def tourism(request):
    return render(request, 'allYouNeed/tourism.html', {'title': 'Tourism'})

def vacation(request):
    return render(request, 'allYouNeed/vacation.html', {'title': 'Vacation'}) 

def entertainment(request):
    return render(request, 'allYouNeed/entertainment.html', {'title': 'Entertainment'}) 


def login(request):
    return render(request, 'allYouNeed/login.html', {'title': 'Login'})                    



