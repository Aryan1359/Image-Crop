
# Create your models here.
from django.db import models

class CroppedImage(models.Model):
    original_name = models.CharField(max_length=255)
    label = models.CharField(max_length=1, choices=[('Q', 'Question'), ('A', 'Answer')])
    saved_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.label}: {self.saved_name}"
