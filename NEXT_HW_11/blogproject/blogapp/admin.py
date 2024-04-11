from django.contrib import admin
from .models import Hobby, Food, Programming,Hobby_Comment,Food_Comment,Programming_Comment,Hobby_cocoment, Food_cocoment,Programming_cocoment
# Register your models here.
admin.site.register(Hobby)
admin.site.register(Food)
admin.site.register(Programming)
admin.site.register(Hobby_Comment)
admin.site.register(Food_Comment)
admin.site.register(Programming_Comment)
admin.site.register(Hobby_cocoment)
admin.site.register(Food_cocoment)
admin.site.register(Programming_cocoment)