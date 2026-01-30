from django.db import models

# Create your models here.
class ScrapedData(models.Model):
    author = models.CharField(max_length=255) # En lugar de title
    quote = models.TextField()               # En lugar de url
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author