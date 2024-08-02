from django.contrib import admin
from . import models

# Register your models here.


class CharacterJobsInline(admin.TabularInline):
    model = models.CharacterJobs

class CharacterJobArmorInline(admin.TabularInline):
    model = models.CharacterJobArmor

class CharacterAdmin(admin.ModelAdmin):
    inlines = [CharacterJobsInline, CharacterJobArmorInline]


admin.site.register(models.Character, CharacterAdmin)
admin.site.register(models.Job)
admin.site.register(models.Spell)
admin.site.register(models.JobArmor)
admin.site.register(models.CharacterJobArmor)
