# -*- coding:utf-8 -*-
from stark.service import stark
from .models import *
from django.forms import ModelForm

class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        labels = {
            "title": '书籍名称',
            "price": '价格',
            'publishDate': '出版日期'
        }

from django.shortcuts import HttpResponse
class BookConfig(stark.ModelStark):

    list_display = ['title', 'price','publishDate', 'publish', 'authors']
    list_display_links = ['title']
    modelform_class = BookModelForm
    search_fields = ['title', 'price']

    def patch_init(self, request, queryset):
        queryset.update(price=123)

        return HttpResponse('批量初始化OK')

    patch_init.short_description = "批量初始化"
    actions = [patch_init]

    list_filter = ['title','publish', 'authors']


stark.site.register(Book, BookConfig)
stark.site.register(Publish)
stark.site.register(Author)
stark.site.register(AuthorDetail)

