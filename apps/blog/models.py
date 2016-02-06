from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse


class Blog(models.Model):
    STATUS_CHOICES = (
        ('d', "draft"),
        ('p', "release"),
    )

    title = models.CharField('Title', max_length=150, db_index=True, unique=True)
    link = models.CharField('Link', max_length=150, default='')
    link.help_text = "Cool URIs don't change"
    snippet = models.CharField('Summary', max_length=500, default='')
    content = models.TextField('Content', )

    add_time = models.DateTimeField('Created', auto_now_add=True)
    publish_time = models.DateTimeField('Issuing Time', null=True)
    update_time = models.DateTimeField('Change the time', auto_now=True)
    status = models.CharField('Status', max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    is_public = models.BooleanField('Public', default=True)
    is_top = models.BooleanField('Sticky', default=False)
    access_count = models.IntegerField('Pageviews', default=1, editable=False)
    category = models.ForeignKey('Category', verbose_name='category')
    tags = models.ManyToManyField('Tag', verbose_name='Label collection', null=True, blank=True)
    tags.help_text = ''
    author = models.ForeignKey(User, verbose_name='Author')

    def save(self, *args, **kwargs):
        self.link = slugify(self.link)
        self.snippet = self.snippet or self.content[:140]
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=(self.id, self.link))

    def __str__(self):
        return self.title


class Category(models.Model):

    title = models.CharField('Name', max_length=50, db_index=True, unique=True)

    class Meta:
        ordering = ['title', ]

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField('Name', max_length=50, db_index=True, unique=True)

    def __str__(self):
        return self.title
