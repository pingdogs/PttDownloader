from django.shortcuts import render, HttpResponse
from .downloadPtt import *
from django.views.generic import TemplateView
from .models import *
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.

class HomePage(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

    	if 'category' in kwargs.keys():
    		articles = self.deal_with_category(request, args, kwargs)
    	elif 'key' in kwargs.keys():
    		articles = self.deal_with_key(request, args, kwargs)
    	else:
    		articles = Article.objects.all()
    	categories = Category.objects.all()
    	keys = KeyWord.objects.all()
    	return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
    	pass
        # if 'to_do' not in request.session:
        #     request.session['to_do'] = []
        # new_item = request.POST.get('new_item')
        # to_do_list = request.session['to_do']
        # to_do_list.append(new_item)
        # request.session['to_do'] = to_do_list

        # return render(request, self.template_name, { 'to_do_list': to_do_list })'
    def deal_with_key(self, request, args, kwargs):
    	key = get_object_or_404(KeyWord, id=kwargs['key'])
    	categories = key.categories.all()
    	articles = Article.objects.filter(category__in=categories, content__contains=key.name)
    	return articles
    	

    def deal_with_category(self, request, args, kwargs):
    	category = kwargs['category']
    	articles = Article.objects.filter(category=Category.objects.get(id=category))
    	return articles
    	



class ArticleDetailPage(TemplateView):
    template_name = 'detail.html'

    def get(self, request, *args, **kwargs):
    	if 'article_id' in kwargs.keys():
	    	article = get_object_or_404(Article, id=kwargs['article_id'])
    	return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
    	pass
        # if 'to_do' not in request.session:
        #     request.session['to_do'] = []
        # new_item = request.POST.get('new_item')
        # to_do_list = request.session['to_do']
        # to_do_list.append(new_item)
        # request.session['to_do'] = to_do_list

        # return render(request, self.template_name, { 'to_do_list': to_do_list })'


