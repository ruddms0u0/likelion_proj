from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


# Create your models here.
