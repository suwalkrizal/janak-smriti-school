from django.contrib import admin
from .models import *

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')  
    search_fields = ('id',)  

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    filter_horizontal = ['images']  # Enables a better UI for ManyToManyField selection

@admin.register(AboutUsImage)
class AboutUsImageAdmin(admin.ModelAdmin):
    list_display = ['image']
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "image":
            kwargs["help_text"] = "Recommended size: 1920 × 600 pixels."
        return super().formfield_for_dbfield(db_field, request, **kwargs)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','author', 'publish_date', 'status')
    search_fields = ('author',)
    list_filter = ( 'author',)

@admin.register(BlogContent)
class BlogContentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'sub_content_title')
    search_fields = ('sub_content_title', 'blog__title')
    list_filter = ('blog',)
    
@admin.register(StudentDetail)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'student_class', 'age')
    list_filter = ('student_class',)
    search_fields = ('name', 'student_id')


@admin.register(TeacherDetail)
class TeacherDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'phone')
    search_fields = ('name', 'subject', 'email')


@admin.register(StaffDetail)
class StaffDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'phone')
    search_fields = ('name', 'position')

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'message')
    search_fields = ('name', 'email')
    list_filter = ('email',) 

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','grade')
    search_fields = ('name',)
    list_filter = ('name','grade')

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    search_fields = ('title',)