from django.contrib import admin
from . import models

# Register your models here.


class CharacterUnlockedJobsInline(admin.TabularInline):
    model = models.CharacterUnlockedJobs

class CharacterAdmin(admin.ModelAdmin):
    inlines = [CharacterUnlockedJobsInline]

admin.site.register(models.Character, CharacterAdmin)
admin.site.register(models.Job)
admin.site.register(models.Spell)
