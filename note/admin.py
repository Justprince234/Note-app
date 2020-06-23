from django.contrib import admin
from . models import Topic, Note
# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ("topic", "note")
    search_fields = ("topic", "note")


admin.site.register(Topic)
admin.site.register(Note, NoteAdmin)
