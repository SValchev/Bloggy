from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    # This can be used in reverse()
    def get_absolute_url(self):
        return reverse('post:info', kwargs={'id':self.id})
