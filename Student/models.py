from django.db import models




class StudentModel(models.Model):
    name = models.CharField(' Name',max_length=200 )
    age = models.IntegerField('Age')
    address=models.TextField()
    email=models.EmailField(default="")
    pin=models.IntegerField(default=0)
    mob=models.IntegerField(default=0)

    def __str__(self):
        return self.name
