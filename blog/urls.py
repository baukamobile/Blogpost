from django.urls import path
from .views import showPost, createBlog, deleteBlog,updateBlog

urlpatterns = [
    path('',showPost, name='showpost'),
    path('create/', createBlog, name='createpost'),
    path('delete/<int:pk>/',deleteBlog, name='deletepost'),
    path('update/<int:pk>/', updateBlog, name='updatepost')


]

