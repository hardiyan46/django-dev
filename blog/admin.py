from django.contrib import admin
from .models import *

#daftarkan kelas yang ada di model
admin.site.register(Author)
admin.site.register(Post)
# Register your models here.
