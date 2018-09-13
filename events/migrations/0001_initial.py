# Generated by Django 2.0.8 on 2018-09-11 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('event', models.CharField(max_length=100)),
                ('prioryt', models.CharField(choices=[('0', 'sem prioridade'), ('1', 'normal'), ('2', 'urgente'), ('3', 'muito urgent'), ('4', 'ultra mega')], max_length=1)),
            ],
        ),
    ]
