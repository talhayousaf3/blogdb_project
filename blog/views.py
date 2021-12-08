from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from easy_pdf.rendering import render_to_pdf_response
# from wkhtmltopdf.views import PDFTemplateView

from blog2_project.tasks import send_email_task
from .models import Post, Comment


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body', 'cover']

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
    fields = ['title', 'body', 'cover']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        prim = self.kwargs.get('pk')
        success_url = f'/post/{prim}/'
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


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'post_comment.html'
    fields = ['comment', ]

    def form_valid(self, form):
        obj = form.save(commit=False)  # this is done to get element before saving it in db.
        obj.author = self.request.user
        obj.post = Post.objects.get(pk=self.kwargs.get('pk'))
        obj.save()

        prim = self.kwargs.get('pk')
        success_url = f'/post/{prim}/'
        return HttpResponseRedirect(success_url)


class LikeUnlikeView(View):

    def get(self, request, pk):

        on_post = Post.objects.get(pk=pk)
        liker = self.request.user
        if liker in on_post.likes.all():
            on_post.likes.remove(liker)
        else:
            on_post.likes.add(liker)

        prim = self.kwargs.get('pk')
        success_url = f'/post/{prim}/'
        return HttpResponseRedirect(success_url)


# def detail_to_pdf(request, pk):
#     template = 'post_detail.html'
#     context = {'post': Post.objects.get(pk=pk)}
#     return render_to_pdf_response(request, template, context)


# class PdfDetail(PDFTemplateView):
#
#     def get_context_data(self, pk):
#         context = {'post': Post.objects.get(pk=pk)}
#         return context
