from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        db_table = 'notes'

    def __str__(self):
        return self.title