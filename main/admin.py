from django.contrib import admin
from .models import TypeArticle, Articles, Comments
# Register your models here.
admin.site.register(TypeArticle)
admin.site.register(Articles)
admin.site.register(Comments)