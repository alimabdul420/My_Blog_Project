from django.urls import path
from App_blog import views

app_name = 'App_blog'
urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create_blog/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug:slug>', views.blog_details, name='blog_details'),
    path('like_post/<pk>/', views.liked, name='like_post'),
    path('unlike_post/<pk>/', views.unliked, name='unlike_post'),
    path('my_blogs/', views.MyBlogs.as_view(), name='my_blogs'),
    path('edit_blog/<pk>/', views.UpdateBlog.as_view(), name='edit_blog'),



]
