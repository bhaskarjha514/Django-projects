from django.db import models

class Notice(models.Model):
    subject = models.CharField(max_length=100)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.subject

# Create your models here.
