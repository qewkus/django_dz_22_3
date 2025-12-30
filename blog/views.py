from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import F # For atomic updates
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 3

    def get_queryset(self):
        # Filter published articles as per README.md
        return super().get_queryset().filter(is_published=True)

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        # Increment view count as per README.md
        obj = super().get_object(queryset)
        obj.views_count = F('views_count') + 1
        obj.save()
        obj.refresh_from_db() # Refresh to get the updated value
        return obj

class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ['title', 'content', 'preview_image', 'is_published'] # Exclude views_count, creation_date

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})

class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ['title', 'content', 'preview_image', 'is_published']

    def get_success_url(self):
        # Redirect to the detail page after successful edit as per README.md
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})

class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('blog:post_list')
