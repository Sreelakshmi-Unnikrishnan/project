from email.mime import image
from django.db import models
from .validators import *
# Create your models here.
class Upload(models.Model):
    image = models.ImageField(upload_to='', verbose_name="image", validators=[validate_image])
    video = models.FileField(upload_to='', verbose_name="video", validators=[validate_video])