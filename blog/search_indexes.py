from haystack import indexes
from blog.models import Post
import datetime

# Create your models here.


class PostIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, 
                            use_template=True)

    content_auto = indexes.EdgeNgramField(model_attr='content')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(last_accessed__lte=datetime.datetime.now())
