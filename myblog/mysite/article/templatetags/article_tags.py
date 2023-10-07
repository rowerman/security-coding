from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

from ..models import ArticlePost
@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()

@register.simple_tag
def author_total_articles(user):
    #注意这里user后的article是定义ArticlePost数据模型类时定义的related_name
    return user.article.count()

@register.inclusion_tag('article/list/latest_articles.html')
def latest_articles(n=5):
    latest_articles = ArticlePost.objects.order_by("-created")[:n]
    return {"latest_articles":latest_articles}

@register.simple_tag
def most_commented_articles(n=3):
    return ArticlePost.objects.annotate(total_comments=Count('comments')).order_by("-total_comments")[:n]
    #这里annotate()函数的含义是添加注释，实际上就是根据Comment与ArticlePost之间的关联，统计每一篇文章的评论数
    #然后将评论数作为注释添加到每一个文章对象上，然后再根据这个注释进行排序筛选

@register.filter(name='markdown')
def markdown_filter(text):
    return mark_safe(markdown.markdown(text))