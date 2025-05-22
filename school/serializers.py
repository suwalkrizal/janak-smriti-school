from rest_framework import serializers
from .models import *


class BannerSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Banner
        fields = '__all__'
    
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None

class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsImage
        fields = ['id','image']

class AboutUsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    class Meta:
        model = AboutUs
        fields = ['id', 'title', 'content','images']
        
    def get_images(self, obj):
        """Return only the first 10 images."""
        images = obj.images.all()[:10]  # Limit to 10 images
        return AboutUsImageSerializer(images, many=True).data

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetail
        fields = '__all__'


class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherDetail
        fields = '__all__'


class StaffDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffDetail
        fields = '__all__'
        
class BlogContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogContent
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    sub_titles = BlogContentSerializer(many=True, source='blogcontent_set')

    class Meta:
        model = BlogPost
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'  # Include all fields

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'