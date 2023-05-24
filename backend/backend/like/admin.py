from django.contrib import admin

from .models import Like, DisLike

admin.site.register(Like)
admin.site.register(DisLike)
