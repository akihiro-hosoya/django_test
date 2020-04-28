from django.views import generic
from .forms import PostCreateForm
from .models import Post, GrandCategory, ParentCategory, Category
from django.views.generic import CreateView, TemplateView, ListView


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

class IndexView(TemplateView):
    template_name = "app/index.html"

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
