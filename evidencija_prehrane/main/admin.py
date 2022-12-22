from django.contrib import admin
from .models import Napomena, Namirnica, Obrok, Osoba, Datum

model_list = [Obrok, Osoba, Datum, Napomena, Namirnica]

admin.site.register(model_list)
