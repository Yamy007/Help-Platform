# Generated by Django 4.1.1 on 2022-11-18 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_remove_question_lvl_result_lvl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='lvl',
            field=models.IntegerField(choices=[(1, 'Very good'), (2, 'Really good'), (3, 'Good'), (4, 'Good Enough'), (5, 'Normal'), (6, 'Kind of bad'), (7, 'Bad'), (8, 'Really bad'), (9, 'Very very bad'), (10, 'Extremely bad')], max_length=20),
        ),
    ]
