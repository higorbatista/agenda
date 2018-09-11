from django.db import models

# Create your models here.

class Event(models.Model):
    priorities_list=(
        ('0','sem prioridade'),
        ('1', 'normal'),
        ('2','urgente'),
        ('3','muito urgent'),
        ('4', 'ultra mega')


    )

    date = models.DateField()
    event = models.CharField(max_length=100)
    prioryt = models.CharField (max_length=1, choices=priorities_list)
