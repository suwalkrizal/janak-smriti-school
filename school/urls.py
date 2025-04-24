from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


# Create Router
router = DefaultRouter()
router.register(r'banner', BannerViewSet, basename='banner')
router.register(r'about', AboutUsViewSet, basename='about')
router.register(r'blog', BlogPostViewSet, basename='blog')
router.register(r'contact', ContactUsViewSet, basename='contact')
router.register(r'testimonial', TestimonialViewSet, basename='testimonial')
router.register(r'offer', OfferViewSet, basename='offer')


# Define URLs
urlpatterns = [
    path('api/', include(router.urls)),  # Include router-generated URLs
    
]