import datetime
import os

from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_images')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Override the save method of the model
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)  # Open image

        # resize image
        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)  # Resize image
            img.save(self.image.path)  # Save it again and override the larger image


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


class category(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name

class brand(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sell(models.Model):
    CONDITION=(('Used','Used'),('New','New'))
    name=models.CharField(max_length=100)
    owner=models.ForeignKey(User, on_delete=models.CASCADE,related_name='items')
    description=models.TextField(max_length=500, null=True)
    condition=models.CharField(max_length=100,choices=CONDITION, null=True)
    price=models.DecimalField(max_digits=15,decimal_places=5)
    category=models.ForeignKey(category, on_delete=models.SET_NULL,null=True)
    brand = models.ForeignKey(brand, on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to ='uploads/',null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    text=models.TextField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Sell,on_delete=models.CASCADE)
