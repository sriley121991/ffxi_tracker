from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Character(models.Model):
    HUME_MALE = "hume_male"
    HUME_FEMALE = "hume_female"
    ELVAAN_MALE = "elvaan_male"
    ELVAAN_FEMALE = "elvaan_female"
    TARUTARU_MALE = "tarutaru_male"
    TARUTARU_FEMALE = "tarutaru_female"
    GALKA = "galka"
    MITHRA = "mithra"
    RACE_CHOICES = [
        (HUME_MALE, 'Hume ♂'),
        (HUME_FEMALE, 'Hume ♀'),
        (ELVAAN_MALE, 'Elvaan ♂'),
        (ELVAAN_FEMALE, 'Elvaan ♀'),
        (TARUTARU_MALE, 'Tarutaru ♂'),
        (TARUTARU_FEMALE, 'Tarutaru ♀'),
        (GALKA, 'Galka'),
        (MITHRA, 'Mithra'),
    ]

    BAHAMUT = 'bahamut'
    SHIVA = 'shiva'
    PHOENIX = 'phoenix'
    CARBUNCLE = 'carbuncle'
    FENRIR = 'fenrir'
    SYLPH = 'sylph'
    VALEFOR = 'valefor'
    LEVIATHAN = 'leviathan'
    ODIN = 'odin'
    QUETZALCOATL = 'quetzalcoatl'
    SIREN = 'siren'
    RAGNAROK = 'ragnarok'
    CERBERUS = 'cerberus'
    BISMARCK = 'bismarck'
    LAKSHMI = 'lakshmi'
    ASURA = 'asura'
    SERVER_CHOICE = [
        (BAHAMUT, 'Bahamut'),
        (SHIVA, 'Shiva'),
        (PHOENIX, 'Phoenix'),
        (CARBUNCLE, 'Carbuncle'),
        (FENRIR, 'Fenrir'),
        (SYLPH, 'Sylph'),
        (VALEFOR, 'Valefor'),
        (LEVIATHAN, 'Leviathan'),
        (ODIN, 'Odin'),
        (QUETZALCOATL, 'Quetzalcoatl'),
        (SIREN, 'Siren'),
        (RAGNAROK, 'Ragnarok'),
        (CERBERUS, 'Cerberus'),
        (BISMARCK, 'Bismarck'),
        (LAKSHMI, 'Lakshmi'),
        (ASURA, 'Asura'),
    ]

    character_name = models.CharField(max_length=25,unique=True)
    race = models.CharField(
        max_length=25,
        choices=RACE_CHOICES,
        default=HUME_MALE
    )
    server = models.CharField(
        max_length=30,
        choices=SERVER_CHOICE,
        default=ASURA
    )

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

class CharacterUnlockedJobsManager(models.Manager):
    def set_default_jobs(self, character_id):
        default_job_list = ['WAR','MNK','WHM','BLM','RDM','THF']
        jobs = Job.objects.all()
        for j in jobs:
            character = character_id
            job = Job.objects.get(pk=j.pk)
            current_level = 1
            unlocked=False
            if j.job_abbreviation in default_job_list:
                unlocked=True
            unlocked_job = self.create(character=character,job=job,unlocked=unlocked,current_level=current_level)
            unlocked_job.save()

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

    objects = CharacterUnlockedJobsManager()

    def __str__(self):
        return ""

class Spell(models.Model):
    spell_name = models.CharField(max_length=50)


    def __str__(self):
        return self.spell_name.title()