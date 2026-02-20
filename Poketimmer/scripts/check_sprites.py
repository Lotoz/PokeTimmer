import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','backend.settings')
import django
django.setup()
from api.models import PokedexEntry
nums=[1,2,25,82,83,95]
for n in nums:
    try:
        p=PokedexEntry.objects.get(numero=n)
        print(n, p.nombre, '->', p.sprite_url, p.sprite_shiny_url)
    except Exception as e:
        print('no entry', n, e)
