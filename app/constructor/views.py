# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from constructor.models import Page, Gallery, Urls
from constructor.serializer import PageSerializer, GallerySerializer, UrlsSerializer


class PageObjectAPI(APIView):

    def get(self, request, **kwargs):
        pages = Page.objects.all()
        pages_json = PageSerializer(pages, many=True).data
        gallery = Gallery.objects.all()
        gallery_json = GallerySerializer(gallery, many=True).data
        urls = Urls.objects.all()
        urls_json = UrlsSerializer(urls, many=True).data
        return Response({'page': pages_json, 'gallery': gallery_json, 'urls': urls_json}, status.HTTP_200_OK)
