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
    # def clean(self):
    #     """Ensure no more than 10 images are attached."""
    #     if self.images.count() > 10:
    #         raise ValidationError("You can only upload up to 10 images.")

    # def save(self, *args, **kwargs):
    #     self.clean()  # Run validation before saving
    #     super().save(*args, **kwargs)
        
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