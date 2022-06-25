from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListViews.as_view(), name="all"),
    path("create/", views.PostCreateViews.as_view(), name="post_create"),
    path("delete/<slug:slug>", views.PostDeleteViews.as_view(), name="post_delete"),
    path("update/<slug:slug>", views.PostUpdateViews.as_view(), name="post_update"),
    path("read/<slug:slug>", views.PostDetailViews.as_view(), name="post_detail"),

]
