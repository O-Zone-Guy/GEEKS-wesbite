from django.db import models


# Blog class
# A class responsible for storing blogs/newsletters
class Blog(models.Model):
    title = models.CharField()
    body = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    last_edit_date = models.DateField(auto_now=True)
    author = models.CharField()
