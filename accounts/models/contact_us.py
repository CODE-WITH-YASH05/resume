from django.db import models


class SchoolMap(models.Model):

    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    map_embed = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.address


class ContactMessage(models.Model):

    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class EmailSettings(models.Model):
    
    email_host = models.CharField(max_length=200, default="smtp.gmail.com")
    email_port = models.IntegerField(default=587)
    email_host_user = models.EmailField()
    email_host_password = models.CharField(max_length=255)
    
    use_tls = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email_host_user 