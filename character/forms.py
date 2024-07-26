from django.forms import ModelForm
from .models import Character, CharacterUnlockedJobs

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ["character_name", "race", "server"]


class UnlockedJobsForm(ModelForm):
    class Meta:
        model = CharacterUnlockedJobs
        fields = '__all__'