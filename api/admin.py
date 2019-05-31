from django.contrib import admin
from api.models import Category,Application
# Register your models here.
class ApplicationInline(admin.TabularInline):
    model = Application
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ApplicationInline]


admin.site.register(Category,CategoryAdmin)
admin.site.register(Application)