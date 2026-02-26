from rest_framework import serializers
from accounts.models import SchoolSettings
from accounts.models import AboutUs
from accounts.models import AlbumImage , Album , GalleryCategory


#school name d
class SchoolSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolSettings
        fields = '__all__'
        
#about_us
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'
        



# ===============================
# GALLERY SERIALIZERS
# ===============================

class AlbumImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumImage
        fields = ['id', 'image']


class AlbumSerializer(serializers.ModelSerializer):
    images = AlbumImageSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'cover_image', 'images']


class GalleryCategorySerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = GalleryCategory
        fields = ['id', 'name', 'albums',]