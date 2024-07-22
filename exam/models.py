from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Question(models.Model):
    OPTION_CHOICE= (
        ('1', 'Option 1'),
        ('2', 'Option 2'),
        ('3', 'Option 3'),
        ('4', 'Option 4')
    )
    title = models.CharField(max_length=500)
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    
class Answer(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    ans = models.TextField(editable=False)

    def __str__(self):
        return self.email




