from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = CloudinaryField('images', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)
    joined = models.DateTimeField(default=timezone.now)

    @classmethod
    def search_profile(cls, name):
        """Method to Search for a user profile"""
        return cls.objects.filter(user__username__icontains=name).all()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        This method will automatically create a user profile using user details provided

        Args:
            sender (_type_): The sender of the signal. This will be triggered by the user
            instance (_type_): instance of user being created
            created (_type_): user profile to be created
        """
        if created:
            Profile.objects.create(user=instance)
        
    @receiver(post_save, sender=user)
    def save_user_profile(sender, instance, **kwargs):
        """This method will save the userprofile instance created"""
        instance.Profile.save

    def __str__(self):
        return f'{self.user.username} Profile'

class Project(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    screenshot = CloudinaryField('images')
    description = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    