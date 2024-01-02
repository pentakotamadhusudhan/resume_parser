from django.db import models


class QuestionsModel(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    created = models.DateField(auto_now_add=True)



class ImageUploadModel(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media')


