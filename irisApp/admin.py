from django.contrib import admin

from .models import *

# Register your models here.

class IrisModelView(admin.ModelAdmin):
	list_display = ["id", 'sepal_length','sepal_width','petal_length','petal_width' , 'prediction']

admin.site.register(IrisModel , IrisModelView)
