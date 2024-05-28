# Generated by Django 4.2.9 on 2024-02-15 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=20)),
                ('job_abbreviation', models.CharField(max_length=3)),
                ('expansion_pack', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterUnlockedJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unlocked', models.BooleanField(default=False)),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.character')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.jobs')),
            ],
        ),
    ]