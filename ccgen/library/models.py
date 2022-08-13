from django.db import models

class DesignInfo(models.Model):
    design_name = models.CharField(max_length=200)
    design_pic = models.ImageField(upload_to='designs')
    likes = models.PositiveIntegerField(default=0)
