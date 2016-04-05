from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView
from blog.models import Post, Tag
from django.utils import timezone
from django.db.utils import IntegrityError

from ipware.ip import get_real_ip, get_ip

import json
from django.http import HttpResponse
from haystack.query import SearchQuerySet

# Create your views here.


def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:5]
    print(request.GET.get('q', ''))
    suggestions = [result.title for result in sqs]
    print(suggestions)
    the_data = json.dumps({
        'results': suggestions
    })
    print(data)
    return HttpResponse(the_data, content_type='application/json')


class PostsListView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'blog/index.html'
    context_object_name = 'my_posts'

    def get_context_data(self, **kwargs):
        context = super(PostsListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context



class PostsListFilteredByTagView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'blog/index.html'
    context_object_name = 'my_posts'

    def get_context_data(self, **kwargs):
        context = super(PostsListFilteredByTagView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, name=self.args[0])
        returned_list = Post.objects.filter(tags=self.tag)
        return returned_list



class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'blog/showpost.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context

    def get_object(self):
        # Call the superclass
        object = super(PostDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        
        try:
            user_ip = get_real_ip(self.request)
            object.last_accessed_ip = user_ip
            object.save()
        except IntegrityError:
            user_ip = get_ip(self.request)
            object.last_accessed_ip = user_ip

        object.save()
        # Return the object
        return object


class About(View):
    def get(self, request):
        return render(request, "blog/about.html", {})

    def post(self):
        pass

