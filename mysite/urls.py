from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic.base import RedirectView

from blog.views import PostsListView, PostDetailView, About, PostsListFilteredByTagView

urlpatterns = [
    # for search. used haystack+whoosh
    url(r'^search/', include('haystack.urls')),

    # ex. localhost:8000/
    url(r'^$', PostsListView.as_view(), name='index_list'),

    # 
    url(r'^blog/page/(?P<page>\d+)/$', PostsListView.as_view(), name='pages'),

    # http://localhost:8000/blog/category/python/
    url(r'blog/category/([\d\w\-]+)/$', PostsListFilteredByTagView.as_view(), name='filter_posts'),

    # ex. localhost:8000/about/
    url(r'about/$', About.as_view(), name='about'),

    # http://localhost:8000/blog/2016/2/16/python-django-haystack/
    url(r'^blog/\d+/\d+/\d+/(?P<slug>[\d\w\-]+)/$', PostDetailView.as_view()),

    # for admin part of site
    url(r'^admin/', admin.site.urls),

    # require for mardown field which used in django admin
    url(r'^markdownx/', include('markdownx.urls')),

]
