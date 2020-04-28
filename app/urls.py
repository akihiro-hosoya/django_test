from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('', views.IndexView.as_view(), name='index'),
    path('post/list/', views.PostListView.as_view(), name='post_list'),
    path('category/<int:category>', views.CaListView.as_view(), name='ca-list'),
]