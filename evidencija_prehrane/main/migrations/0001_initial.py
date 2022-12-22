# Generated by Django 4.1.4 on 2022-12-22 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Namirnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namirnica_povrce', models.CharField(default=None, max_length=30)),
                ('namirnica_voce', models.CharField(default=None, max_length=30)),
                ('namirnica_meso', models.CharField(default=None, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Napomena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('napomena_lijekovi', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osoba_ime', models.CharField(default=None, max_length=30)),
                ('osoba_prezime', models.CharField(default=None, max_length=30)),
                ('osoba_napomena', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.napomena')),
            ],
        ),
        migrations.CreateModel(
            name='Obrok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obrok_zajutrak', models.CharField(default=None, max_length=50)),
                ('obrok_dorucak', models.CharField(default=None, max_length=50)),
                ('obrok_rucak', models.CharField(default=None, max_length=50)),
                ('obrok_uzina', models.CharField(default=None, max_length=50)),
                ('obrok_vecera', models.CharField(default=None, max_length=50)),
                ('obrok_namirnice', models.ManyToManyField(to='main.namirnica')),
                ('obrok_od_osobe', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.osoba')),
            ],
        ),
        migrations.CreateModel(
            name='Datum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum_dan', models.CharField(choices=[('PON', 'Ponedjeljak'), ('UTO', 'Utorak'), ('SRI', 'Srijeda'), ('CET', 'Četvrtak'), ('PET', 'Petak'), ('SUB', 'Subota'), ('NED', 'Nedjelja')], max_length=10)),
                ('datum_obroka', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.obrok')),
            ],
        ),
    ]
