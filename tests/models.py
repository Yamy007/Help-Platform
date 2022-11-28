from django.db import models

# Create your models here.Test

class Test(models.Model):
    title = models.CharField(max_length = 25)
    def __str__(self):
        return self.title
    
    
class Question(models.Model):
    question = models.CharField(max_length = 255)
    test = models.ForeignKey(Test, on_delete = models.CASCADE)
    def __str__(self):
        return self.question


class Result(models.Model):
    title = models.CharField(max_length = 255)
    test = models.ForeignKey(Test, on_delete = models.CASCADE)
    lvl_choice =[(1,'Very good'), (2, 'Really good'), (3, 'Good'), (4, 'Good Enough'), (5, 'Normal'), (6, 'Kind of bad'), (7, 'Bad'), (8, 'Really bad'), (9, 'Very very bad'), (10, 'Extremely bad') ]
    lvl = models.IntegerField(max_length=20, choices = lvl_choice)
    def __str__(self):
        return self.title    