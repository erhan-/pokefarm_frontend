from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Account)
admin.site.register(Connection)
admin.site.register(Statistics)
admin.site.register(Eggs)
admin.site.register(Profile)
admin.site.register(PokeData)

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('pokemon_id', 'individual_id')
    pass

admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(InventoryItem)
admin.site.register(ItemData)
