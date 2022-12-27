from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify
from movie.models import Movie

# Create your models here.

class Profile(models.Model):
    def image_upload(instance, filename):
        image_name = slugify(instance.user.username)
        image_list = filename.split(".")
        extension = image_list[len(image_list)-1]
        return "static/images/users/%s.%s"%(image_name, extension)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to=image_upload, max_length=255)
    job = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.user.user)