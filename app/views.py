from django.views import generic
from .forms import PostCreateForm
from .models import Post, GrandCategory, ParentCategory, Category
from django.views.generic import CreateView, TemplateView, ListView
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from functools import reduce
from operator import and_

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "app/post_form.html"
    redirect_field_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grandcategory_list'] = GrandCategory.objects.all()
        context['parentcategory_list'] = ParentCategory.objects.all()
        return context
class ResultView(ListView):
    model = Post
    template_name = 'app/result.html'
    def get_queryset(self):
        queryset = Post.objects.order_by('-id')
        keyword = self.request.GET.get('keyword')
        if keyword:
            exclusion = set([' ', '　'])
            q_list = ''
            for i in keyword:
                if i in exclusion:
                    pass
                else:
                    q_list += i
            query = reduce(
                        and_, [Q(title__icontains=q) for q in q_list]
                    )
            queryset = queryset.filter(query)
            messages.success(self.request, '「{}」の検索結果'.format(keyword))
        return queryset

class IndexView(ListView):
    model = Post
    template_name = 'app/index.html'

class PostListView(ListView):
    model = Post
    template_name = 'app/post_list.html'

    def get_queryset(self):
        return Post.objects.all()

class CaListView(ListView):
    model = Post
    template_name = "app/post_list.html"

    def get_queryset(self):
        category = Category.objects.get(id=self.kwargs['category'])
        queryset = Post.objects.order_by('-id').filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_key'] = self.kwargs['category']
        return context