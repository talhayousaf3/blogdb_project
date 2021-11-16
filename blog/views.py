from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from blog2_project.tasks import send_email_task


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        blog_creator = self.request.user
        send_email_task.delay(blog_creator.id)
        success_url = reverse_lazy('home')
        return HttpResponseRedirect(success_url)


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        success_url = reverse_lazy('home')
        return HttpResponseRedirect(success_url)


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class FollowView(View):

    def get(self, request, pk):
        author = Post.objects.get(pk=pk).author
        followers = self.request.user

        if author in followers.following.all():
            followers.following.remove(author)
            author.follower.remove(followers)

        else:
            followers.following.add(author)
            author.follower.add(followers)

        success_url = reverse_lazy('home')
        return HttpResponseRedirect(success_url)


def check_follower(request):
    return render(request, 'check_followers.html')


def check_following(request):
    return render(request, 'check_following.html')
