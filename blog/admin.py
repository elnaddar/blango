from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title", )}
  list_display = ("title", "slug", "published_at")
admin.site.register(models.Tag)
admin.site.register(models.Post, PostAdmin)

