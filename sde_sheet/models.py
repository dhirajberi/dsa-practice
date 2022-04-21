from django.db import models

# Create your models here.
class DSA(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Question(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    ds = models.ForeignKey(DSA, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag)
    solved = models.BooleanField(default=False)

    def __str__(self):
        return self.name