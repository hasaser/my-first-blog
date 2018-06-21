
from django.contrib import admin
from .models import Post  


class PostAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'tarih']
    list_display_links = ['tarih']
    list_filter = ['tarih']
    search_fields = ['baslik', 'icerik']
    list_editable = ['baslik']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)