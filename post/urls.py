from django.urls import path
from . import views


app_name = 'post'

urlpatterns = [
    # post views
    path('', views.list_posts, name="post_list"),
]
