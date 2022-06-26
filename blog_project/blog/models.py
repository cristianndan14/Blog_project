from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=155)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank = False, null = False, max_length=60000)

    def __str__(self):
        return f'{self.title} -- {self.date} -- Autor  '
