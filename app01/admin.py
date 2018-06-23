from django.contrib import admin

# Register your models here.

from .models import *


class BookConfig(admin.ModelAdmin):
    list_display = ['title', 'price', 'publish']
    list_filter = ['title', 'publish', 'authors']
    # list_display_links = ['price']
    def patch_init(self, request, queryset):
        print(queryset)   # <QuerySet [<Book: shu 2>, <Book: gOy>]>
        queryset.update(price=100)

    patch_init.short_description = '批量初始化'

    actions = [patch_init]


admin.site.register(Book, BookConfig)
admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Publish)

