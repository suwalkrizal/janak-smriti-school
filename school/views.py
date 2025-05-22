from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination
from django.core.mail import send_mail
from django.conf import settings
import threading

from .models import *
from .serializers import *
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import DjangoModelPermissions

# Pagination class
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            "total_data": self.page.paginator.count,  # Total number of records
            "next": self.get_next_link(),  # URL for the next page
            "previous": self.get_previous_link(),  # URL for the previous page
            "data": data,  # Paginated data
        })

# Function to send email in the background
def send_email_background(subject, message, recipient_email):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [recipient_email],
        fail_silently=False,
    )

class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    pagination_class = CustomPagination

class AboutUsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    pagination_class = CustomPagination
    
    
class AboutUsImageViewSet(ReadOnlyModelViewSet):  
    queryset = AboutUsImage.objects.all()
    serializer_class = AboutUsImageSerializer
    pagination_class = CustomPagination

class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    pagination_class = CustomPagination

class BlogContentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogContent.objects.all()
    serializer_class = BlogContentSerializer
    pagination_class = CustomPagination

class StudentDetailViewSet(viewsets.ModelViewSet):
    queryset = StudentDetail.objects.all()
    serializer_class = StudentDetailSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'post']
    permission_classes = [DjangoModelPermissions]



class TeacherDetailViewSet(viewsets.ModelViewSet):
    queryset = TeacherDetail.objects.all()
    serializer_class = TeacherDetailSerializer
    pagination_class = CustomPagination
    permission_classes = [DjangoModelPermissions]


class StaffDetailViewSet(viewsets.ModelViewSet):
    queryset = StaffDetail.objects.all()
    serializer_class = StaffDetailSerializer
    pagination_class = CustomPagination
    permission_classes = [DjangoModelPermissions]

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            
            # Email subject & message
            subject = "Thank You for Contacting Us"
            email_message = f"Hello {contact.name},\n\nWe have received your message:\n\n{contact.message}\n\nWe will get back to you soon!"
            
            # Send email in the background
            thread = threading.Thread(target=send_email_background, args=(subject, email_message, contact.email))
            thread.start()
            
            return Response({"message": "Message sent successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    pagination_class = CustomPagination

class OfferViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    pagination_class = CustomPagination