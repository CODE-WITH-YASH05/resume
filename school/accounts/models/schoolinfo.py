from django.db import models

class SchoolSettings(models.Model):
    school_name = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    logo = models.ImageField(upload_to='school_logo/')

    def __str__(self):
        return self.school_name