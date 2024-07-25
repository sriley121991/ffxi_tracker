from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from . import models
from .forms import CharacterForm

# Create your views here.
def characters(request):
    character_list = models.Character.objects.all
    context = {
        "character_list": character_list,
    }
    return render(request, "characters/characters.html", context)

def character_detail(request, character_name):
    job_list = models.CharacterUnlockedJobs.objects.filter(character__character_name=character_name)
    context = {"job_list": job_list}
    return render(request, "characters/character_details.html", context)

def new_character(request):
    # if request.method == "POST":
    #     form = CharacterForm(request.POST)
    #     form.save()
    # else:
    #     form = CharacterForm()
    context = {}
    return render(request, "characters/new_character.html", context)