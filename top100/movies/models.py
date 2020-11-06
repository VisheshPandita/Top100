from django.db import models
from users.models import Profile

# Create your models here.
class Movies(models.Model):
    movie = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)