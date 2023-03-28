from django.db import models


class Registration(models.Model):
    First_Name = models.CharField(max_length=20, blank=True)
    Last_Name = models.CharField(max_length=20, blank=True)
    DOB = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.First_Name
