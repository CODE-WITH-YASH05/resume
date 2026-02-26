from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import GalleryCategory, Album
from accounts.serializers import (
    GalleryCategorySerializer,
    AlbumSerializer
)


@api_view(['GET'])
def gallery_categories(request):
    categories = GalleryCategory.objects.prefetch_related('albums__images')
    serializer = GalleryCategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def albums_by_category(request, category_name):

    if category_name.lower() == "all":
        albums = Album.objects.all().prefetch_related('images')
    else:
        albums = Album.objects.filter(
            category__name__iexact=category_name
        ).prefetch_related('images')

    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)