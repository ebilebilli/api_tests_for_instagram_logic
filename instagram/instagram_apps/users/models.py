from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    OPEN_PROFILE = 'Open Profile'
    PRIVATE_PROFILE = 'Private Profile'

    STATUS_LIST = [
        (OPEN_PROFILE, 'Open Profile'),
        (PRIVATE_PROFILE, 'Private Profile')
]
    profile_status = models.CharField(max_length=25, choices=STATUS_LIST, default=OPEN_PROFILE)
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=155, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile/pictures', null=True, blank=True)
   
    @property
    def followers_count(self):
        return self.followers.count() 
    
    @property
    def followings_count(self):
        return self.followings.count()

    def __str__(self):
        return self.username