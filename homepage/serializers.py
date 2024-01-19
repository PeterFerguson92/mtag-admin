from rest_framework import serializers
from .models import Banner, Homepage


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
        
class HomepageSerializer(serializers.ModelSerializer):
    banners = BannerSerializer(many=True, read_only=True)

    class Meta:
        model = Homepage
        fields = "__all__"