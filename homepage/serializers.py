from rest_framework import serializers
from .models import Banner, Block, Homepage


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = "__all__"
        
class HomepageSerializer(serializers.ModelSerializer):
    banners = BannerSerializer(many=True, read_only=True)
    blocks = BlockSerializer(many=True, read_only=True)
    
    class Meta:
        model = Homepage
        fields = "__all__"