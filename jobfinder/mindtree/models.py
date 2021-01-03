from django.db import models

# Create your models here.


class Job(models.Model):

    id=models.CharField(max_length=50,primary_key=True)

    title=models.CharField(max_length=50)
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.title
