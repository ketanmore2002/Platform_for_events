# Generated by Django 4.1.1 on 2022-10-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0049_remove_host_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='rank',
            field=models.CharField(blank=True, default='active', max_length=300, null=True),
        ),
    ]
