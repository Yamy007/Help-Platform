# Generated by Django 4.1 on 2022-10-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typearticle',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]