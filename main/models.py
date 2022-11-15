from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TypeArticle(models.Model):
    type_article = models.CharField(max_length = 25)
    description = models.CharField(max_length = 255, blank=True)
    level = models.IntegerField(default = 0)
    def __str__(self):
        return self.type_article


class Articles(models.Model):
    types  = models.ForeignKey(TypeArticle, on_delete = models.CASCADE)
    title  = models.CharField(max_length = 25)
    link_for_image = models.CharField(max_length = 255, default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.jssor.com%2Fdemos%2Fimage-slider.slider&psig=AOvVaw0yLA41bsKX6tX66LWF7k37&ust=1667140785778000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCIDy19zVhfsCFQAAAAAdAAAAABAG")
    text = models.TextField()
    time = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    title = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.ForeignKey(Articles, on_delete = models.CASCADE) 
    time = models.DateTimeField(auto_now_add = True)
    text = models.TextField()
    def __str__(self):
        return self.text