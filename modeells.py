from django.db import models

class data(models.Model):
    _id = models.CharField(max_length=250)
    service = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    media = models.CharField(max_length=250)
    tags = models.CharField(max_length=250)
    categories = models.CharField(max_length=250)
    end_time = models.CharField(max_length=250)

class base(models.Model):
    data = models.ForeignKey(data,on_delete=models.CASCADE)
    fill_type = models.CharField(max_length=250)