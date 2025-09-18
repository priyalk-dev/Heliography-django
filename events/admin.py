from django.contrib import admin
from .models import Category,Events
from django.utils.html import format_html
# Register your models here.

class PhotoInline(admin.TabularInline):
    model = Events
    extra =1
    readonly_fields=('image_preview',)
    
    def image_preview(self,obj):
        if obj.image:
            return format_html('<img src="{}" width="120" height="120" style="object-fit:cover;" />', obj.image.url)
        return 'No Image'
    image_preview.short_description ="preview"
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    inlines = [PhotoInline]
    
    
@admin.register(Events)
class PhotoAdmin(admin.ModelAdmin):
    list_display=('id','category','image_preview')
    readonly_fields=('image_preview',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="120" height="120" style="object-fit:cover;" />', obj.image.url)
        return "(No Image)"

    image_preview.short_description = "Preview"
    
