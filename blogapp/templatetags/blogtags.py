from django import template
from blogapp.models import Post

register = template.Library()

@register.simple_tag
def show_dates():
    dates = ["<li><a href='/%s/%s'>%s</a></li>" % (p.created.year, p.created.month,p.created.strftime("%B %Y")) for p in Post.objects.all()]
    dateset = []
    for d in dates:
        if not d in dateset:
            dateset.append(d)
    return "\n".join(dateset)

@register.simple_tag
def show_categories():
    posts = Post.objects.all()
    cats = []
    for post in posts:
        cats += post.category.lower().split(",")
        
    cats = sorted(set(cats))

    return "\n".join(["<li><a href='/category/%s'>%s</a></li>" % (c.lower(), c.title()) for c in cats])
    
    
