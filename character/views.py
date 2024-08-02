from django.shortcuts import render, redirect
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
    character = models.Character.objects.get(character_name=character_name)
    jobs = models.Job.objects.all()
    job_list = models.CharacterJobs.objects.filter(character__character_name=character_name)
    # armor_list = models.JobArmor.objects.filter(jobs.pk)
    context = {
        "job_list": job_list,
        "character": character,
        # "armor_list": armor_list,
    }
    return render(request, "characters/character_details.html", context)

def new_character(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        form.save()

        char = models.Character.objects.get(character_name=form.data.get('character_name'))
        models.CharacterJobs.objects.set_default_jobs(char)
        return redirect("characters:characters")
    else:
        form = CharacterForm()
    context = {"form": form}
    return render(request, "characters/new_character.html", context)

def update_character(request, character_name):
    character = models.Character.objects.get(character_name=character_name)

    if request.method == "POST":
        character_form = CharacterForm(request.POST, instance=character)
        if character_form.is_valid():
            character_form.save()
            return redirect("characters:character_details", character.character_name)
    else:    
        character_form = CharacterForm(instance=character)
    context = {"character_form":character_form}
    return render(request, "characters/update_character.html", context)