from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} - {self.title[:20]}'