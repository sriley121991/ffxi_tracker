from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Character(models.Model):
    character_name = models.CharField(max_length=25)
    race = models.CharField(max_length=25)
    server = models.CharField(max_length=30)

    def __str__(self):
        return self.character_name

class Job(models.Model):
    FINAL_FANTASY_XI = "ffxi"
    RISE_OF_THE_ZILART = "RotZ"
    TREASURES_OF_AHT_URHGAN = "ToAU"
    WINGS_OF_THE_GODDESS = "WotG"
    SEEKERS_OF_ADOULIN = "SoA"
    EXPANSION_PACK_CHOICES = [
        (FINAL_FANTASY_XI, "Final Fantasy XI"),
        (RISE_OF_THE_ZILART, "Rise of the Zilart"),
        (TREASURES_OF_AHT_URHGAN, "Treasures of Aht Urhgan"),
        (WINGS_OF_THE_GODDESS, "Wings of the Goddess"),
        (SEEKERS_OF_ADOULIN, "Seekers of Adoulin"),
    ]

    job_name = models.CharField(max_length=20)
    job_abbreviation = models.CharField(max_length=3)
    expansion_pack = models.CharField(
        max_length=4,
        choices=EXPANSION_PACK_CHOICES,
        default=FINAL_FANTASY_XI,
    )

    def __str__(self):
        return self.job_abbreviation.upper()

class CharacterUnlockedJobs(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    unlocked = models.BooleanField(default=False)
    current_level = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(99),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return ""

class Spell(models.Model):
    spell_name = models.CharField(max_length=50)


    def __str__(self):
        return self.spell_name.title()