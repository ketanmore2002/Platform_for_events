# Generated by Django 4.1.1 on 2022-10-06 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0050_alter_events_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='entry',
            field=models.CharField(blank=True, default='active', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='rank',
            field=models.CharField(blank=True, default='1', max_length=300, null=True),
        ),
    ]
