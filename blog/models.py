from django.db import models
from django.core.urlresolvers import reverse
from markdownx.models import MarkdownxField
from slugify import slugify
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=127, verbose_name='Назва тегу')

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=255, 
                            verbose_name='Назва')

    slug = models.SlugField(unique=True, 
                            max_length=255, 
                            blank=True, 
                            verbose_name='Slug')

    description = models.CharField(max_length=255, 
                                verbose_name='Короткий опис')

    description_image = models.CharField(max_length=255, 
                                        default="https://images.unsplash.com/photo-1447069387593-a5de0862481e?crop=entropy&fit=crop&fm=jpg&h=675&ixjsv=2.1.0&ixlib=rb-0.3.5&q=80&w=1375")

    content = MarkdownxField(verbose_name='Контент')                              # models.TextField()

    published = models.BooleanField(default=True, 
                                    verbose_name='Опубліковано?')

    created = models.DateTimeField(auto_now_add=True, 
                                    verbose_name='Дата створення')

    last_accessed = models.DateTimeField(verbose_name='Останній перегляд')

    last_accessed_ip = models.GenericIPAddressField(default='127.0.0.1', 
                                                    verbose_name='IP-адреса останнього відвідувача')

    original_link = models.URLField(default='', 
                                    verbose_name='Посилання на оригінал')

    author = models.ForeignKey(User, default=1, 
                                verbose_name='Автор')

    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/blog/{0}/{1}/{2}/{3}/".format(self.created.year, self.created.month, self.created.day, self.slug)

