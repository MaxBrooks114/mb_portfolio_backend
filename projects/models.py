from django.db import models

# Create your models here.
class Project(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    repo_link = models.URLField()
    demo = models.URLField(blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.name