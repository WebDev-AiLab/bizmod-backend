from django.contrib import admin

# Register your models here.


from constructor.models import Order, TypePage, Page, Gallery, Urls


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('nomber',)


@admin.register(TypePage)
class TypePageAdmin(admin.ModelAdmin):
    list_display = ('name', )


class GalleryInline(admin.StackedInline):
    model = Gallery

class UrlsInline(admin.StackedInline):
    model = Urls


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('type_page', 'order')
    inlines = [GalleryInline, UrlsInline]
