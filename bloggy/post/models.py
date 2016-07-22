from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_path(self):
        return reverse('post:info', kwargs={'id':self.id})
