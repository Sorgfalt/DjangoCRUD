from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=300)

    class Meta:
        db_table = 'board'
