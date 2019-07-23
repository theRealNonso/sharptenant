from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.TextField(null=True)
    street_name = models.CharField(max_length=100)
    house_number = models.IntegerField()
    location = models.CharField(max_length=100, null=True)
    review = models.TextField() 
    image = models.FileField(upload_to='images/', default='images/dummy.jpg')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("Address: " + self.street_name)
    # overtime there will be an image field here


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.user)
