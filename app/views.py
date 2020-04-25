from django.views import generic
from .forms import PostCreateForm
from .models import Post, GrandCategory, ParentCategory
from django.views.generic import CreateView


class PostCreate(CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = '/'  # reverse_lazy等のほうが良い。これは手抜き

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grandcategory_list'] = GrandCategory.objects.all()
        context['parentcategory_list'] = ParentCategory.objects.all()
        return context
