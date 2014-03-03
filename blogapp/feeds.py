from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blogapp.models import Post

class RSSFeed(Feed):
    title = "Personal Blog of Rob Sayers"
    link = "/"
    description = ""

    def items(self):
        return Post.objects.all()[:10]

    def item_title(self,item):
        return item.title

    def item_description(self,item):
        return item.html()

    def item_link(self,item):
        return "/%s/%s/%s" % (item.created.year, item.created.month, item.slug)

    def item_pubdate(self,item):
        return item.created
