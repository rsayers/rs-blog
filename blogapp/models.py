from django.db import models

# Create your models here.

from django.db import models
from django.core.urlresolvers import reverse
import markdown
     
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    #description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    #    tags = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['-created']
        
    def __unicode__(self):
        return u'%s' % self.title
        
    def get_formatted_content(self):
        return self.content.replace("\n","<br/>")

    def get_absolute_url(self):
        return "%d/%d/%s" % (self.created.year, self.created.month, self.slug)
        return reverse('blogapp.views.post', args=[self.created.year, self,created.month,self.slug])

    def html(self):
        return markdown.markdown(self.content)
