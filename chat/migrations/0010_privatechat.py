# Generated by Django 4.1 on 2022-11-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_room_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_1', models.CharField(max_length=255)),
                ('user_2', models.CharField(max_length=255)),
                ('name_hash', models.CharField(max_length=255)),
            ],
        ),
    ]
