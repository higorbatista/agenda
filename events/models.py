from django.db import models
from django.utils import timezone
from libgravatar import Gravatar

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

    class Meta:
            ordering = ('-date' , '-prioryt','event')

    def number_of_comments(self):
        return self.number_of_comments()

    def __str__(self):
        return self.event

class Comment(models.Model):
    """"comentario efetuado em um detetrminado evento"""

    author =models.CharField (max_length=80)
    email = models.EmailField()
    text = models.CharField(max_length=160)
    commented = models.DateTimeField(default=timezone.now)
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                                    related_name='commment_event')

    """Retormar a partir do enedereço de emeail, um avatar configurado no Gravatar"""
    def avatar(self):
        g = Gravatar (self.email)
        return g.get_image(defalt='identicon')

    def __str__(self):
        return "{} comentou em {:%c}".format(self.author, self.commented)