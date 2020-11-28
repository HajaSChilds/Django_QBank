from django.db import models

# Create your models here.
class Question(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    topic = models.CharField(max_length=100)
    question = models.CharField(max_length=300)
    submitted = models.DateTimeField(auto_now_add=True)
    answer = models.CharField(max_length=1000, blank=True)


    def __str__(self):
        return self.question