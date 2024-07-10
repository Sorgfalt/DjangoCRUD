from django.db import models


class BoardTest(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=300)
    published_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'boardTest'
