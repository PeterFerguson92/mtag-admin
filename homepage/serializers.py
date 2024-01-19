from rest_framework import serializers
from .models import AboutUs, Banner, Block, Details, Homepage, Media, Video


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = "__all__"

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"
        
class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = "__all__"
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class MediaSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = Media
        fields = "__all__"
        
class HomepageSerializer(serializers.ModelSerializer):
    banners = BannerSerializer(many=True, read_only=True)
    blocks = BlockSerializer(many=True, read_only=True)
    aboutUs = AboutUsSerializer(many=False, read_only=True)
    details = DetailSerializer(many=False, read_only=True)
    media = MediaSerializer(many=False, read_only=True)
    class Meta:
        model = Homepage
        fields = "__all__"