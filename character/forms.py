from django.forms import ModelForm
from .models import Character, CharacterJobs

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ["character_name", "race", "server"]


class UnlockedJobsForm(ModelForm):
    class Meta:
        model = CharacterJobs
        fields = '__all__'