from django.shortcuts import render
from django.views import View
from .models import Article


class NewsView(View):
    template_name = ''

    def get(self, request):
        articles = Article.objects.all()
        context = {
            'articles' : articles
        }
        return render(request, self.template_name, context)


class NewsDetailView(View):
    template_name = ''

    def get(self, request, news_id):
        article = Article.objects.get(pk=news_id)
        context = {
            'article': article
        }
        return render(request, self.template_name, context)


