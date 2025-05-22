from django.db import models
from ckeditor.fields import RichTextField 
from django.utils import timezone
# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return f"Banner: {self.image.name}" if self.image else "No Image Available"

class AboutUsImage(models.Model):
    image = models.ImageField(upload_to='about_us/')

    def __str__(self):
        return self.image.url

class AboutUs(models.Model):
    title = models.CharField(max_length=225)
    content = RichTextField()
    images = models.ManyToManyField(AboutUsImage, related_name='about_us')
        
    def __str__(self):
        return self.title

class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=225, unique=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    publish_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    # content =RichTextField()

    def __str__(self):
        return self.title

class BlogContent(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    sub_content_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog_images/', height_field=None, width_field=None, max_length=None)
    sub_content = RichTextField()

    def __str__(self):
        return f"{self.blog.title} - {self.sub_content_title}"


class StudentDetail(models.Model):
    CLASS_CHOICES = [
        ('Nursery', 'Nursery'),
        ('LKG', 'LKG'),
        ('UKG', 'UKG'),
        ('1', 'Class 1'),
        ('2', 'Class 2'),
        ('3', 'Class 3'),
        ('4', 'Class 4'),
        ('5', 'Class 5'),
        ('6', 'Class 6'),
        ('7', 'Class 7'),
        ('8', 'Class 8'),
        ('9', 'Class 9'),
        ('10', 'Class 10'),
    ]

    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50, unique=True)
    student_class = models.CharField(max_length=20, choices=CLASS_CHOICES)
    age = models.IntegerField()
    address = models.CharField(blank=True, null=True)
    image = models.ImageField(upload_to='students/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_student_class_display()})"

class TeacherDetail(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='teachers/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class StaffDetail(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)  # e.g., Accountant, Janitor, Librarian
    phone = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='staff/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.position}"
    
# Contact Model
class ContactUs(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    phone = models.CharField(max_length=225, blank=True, null=True)
    message = RichTextField()

    def __str__(self):
        return f"{self.name} - {self.email}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=50)
    message = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

class Offer(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title