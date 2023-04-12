from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


class BlogPageView(View):
    def get(self, request):
        """ View for contacts """
        context={}
        return render(request, 'blog-page.html', context=context)

class BlogSinglePageView(View):
    def get(self, request, blog_id):
        """ View for contacts """
        context={}
        return render(request, 'blog-single-page.html', context=context)