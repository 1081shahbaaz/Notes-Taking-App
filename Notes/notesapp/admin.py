from xml.dom.minidom import Document
from django.contrib import admin
from .models import Document, Profile

# Register your models here.
admin.site.register(Document)
admin.site.register(Profile)

