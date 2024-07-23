from django.db import models

# Create your models here.
class Winner(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='winners/', null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Winners'

class Core(models.Model):
    exam_password = models.CharField(max_length=100)

    def __str__(self):
        return self.exam_password