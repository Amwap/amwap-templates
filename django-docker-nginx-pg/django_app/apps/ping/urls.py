from django.urls import path
from django.urls.conf import include

from apps.blog.views import BlogPageView, BlogSinglePageView

urlpatterns = [
    path('blog/', BlogPageView.as_view(), name='blog-page'),
    path('blog/<slug:blog_id>', BlogSinglePageView.as_view(), name='blog-single-page'),
]