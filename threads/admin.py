from django.contrib import admin
from .models import Thread, Subject, Post
# Register your models here.
admin.site.register(Subject)
admin.site.register(Post)
admin.site.register(Thread)
