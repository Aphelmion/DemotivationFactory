from django.db import models

# Create your models here.
class Demotivator(models.Model):
    class Meta():
        db_table = 'demotivator'

    demotivator_name = models.CharField(max_length=100)
    demotivator_date = models.DateTimeField()
    demotivator_likes = models.IntegerField(default=0)
