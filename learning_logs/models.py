from django.db import models
from django.contrib.auth.models import User


class Section(models.Model):
    """Model Section of the theme being created"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return the string representation of the model in the admin"""
        return self.text


class Model(models.Model):
    """Model with name Model of the model being related to the Section"""
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=True)
    text = models.TextField(max_length=5000, blank=False, null=True)
    image = models.ImageField(upload_to='images/', blank=False, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "models"

    def __str__(self):
        """Return the string representation of the model in the admin and
        if the text is more than 200 characters, then show only 50"""
        if len(self.text) > 200:
            return f"{self.text[:50]}..."
        else:
            return self.text

