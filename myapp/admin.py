from django.contrib import admin
from .models import Post

admin.site.register(Post)

# python manage.py makemigrations myapp
# python manage.py migrate myapp
