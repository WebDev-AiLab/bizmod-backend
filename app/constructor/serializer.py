from rest_framework import serializers

from constructor.models import Page, TypePage, Order, Gallery, Urls


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'page', 'image')


class TypePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePage
        fields = ('name',)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'nomber',)

class UrlsSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Urls
        fields = ('__all__')


class PageSerializer(serializers.ModelSerializer):
    type_page = TypePageSerializer()
    order = OrderSerializer()

    class Meta:
        model = Page
        fields = '__all__'
