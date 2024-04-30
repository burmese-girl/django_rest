from django.urls import path
from . import views

urlpatterns = [
    path("blogpost/",views.BlogPostListCreate.as_view(),name="blogpost-view-create"),
    path("blogpost/<int:pk>",views.BlogPostRetrieveUpdateDestroy.as_view(),name="update"),
    path("blogposts-views",views.BlogPostList.as_view(),name="blogposts-views")
]
