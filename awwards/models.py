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
    contact = models.CharField(max_length=12,blank=True)
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
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)
    date_added = models.DateTimeField(default=timezone.now)
    
    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()
        
    @classmethod
    def all_projects(cls):
        return cls.objects.all()
         

    @classmethod
    def search_projects(cls, search_term):
        return cls.objects.filter(title__icontains=search_term).all()
         
    
    def __str__(self):
        return f'{self.title} Project'

class Review(models.Model):
    userRatings = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    projects = models.ForeignKey(Project,on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True)
    review = models.TextField(max_length=1500,blank=True)
    design = models.PositiveSmallIntegerField(choices = userRatings, default= 0)
    usability = models.PositiveSmallIntegerField(choices = userRatings, default = 0)
    content = models.PositiveSmallIntegerField(choices = userRatings, default = 0)
    
    def save_review(self):
        self.save()

    @classmethod
    def get_review(cls, id):
        return Review.objects.filter(post_id=id).all()
         
    def __str__(self):
        return f'{self.review} Review'