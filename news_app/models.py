from django.db import models


class news_datas (models.Model):
    title=models.TextField(max_length=100)
    contact=models.TextField(max_length=100)
    catagory=models.TextField(max_length=100)
    date=models.TextField(max_length=20)
    image=models.ImageField('media/')
    


    

# Create your models here.
