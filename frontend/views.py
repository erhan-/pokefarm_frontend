from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import requests
import json


# Models
from .models import Profile, InventoryItem, Pokemon, PokeData, ItemData, Statistics


# Views
def get_location(profile):
    url = 'http://'+profile.connection.hostname+':'+str(profile.connection.port)+'/position'
    location = requests.get(url).json()
    return location

class PokeList(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(id=kwargs['account_id'])
        location = get_location(profile)
        inventory = InventoryItem.objects.filter(owner=profile).order_by('-count','-poke_data__cp')
        return render(request, 'poke_list.html', {'inventory_list': inventory, 'profile': profile, 'location': location })


class Sync(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(id=kwargs['account_id'])
        url = 'http://'+profile.connection.hostname+':'+str(profile.connection.port)+'/inventory'
        inventory_items = requests.get(url).json()

        # Clear Database

        # Clear all items of this profile
        InventoryItem.objects.filter(owner=profile).delete()



        for inventory_item in inventory_items:
            if "pokemon_data" in inventory_item['inventory_item_data']:
                poke_list = inventory_item['inventory_item_data']['pokemon_data']

                # Create Pokedata objects
                pokedata, created = PokeData.objects.get_or_create(
                    poke_id = poke_list.get('pokemon_id',0),
                )

                # Creating Pokemon objects if not exists
                pokemon, created = Pokemon.objects.get_or_create(
                    individual_id = poke_list.get('id','0'),
                    poke_data = pokedata,
                    pokemon_id = poke_list.get('pokemon_id',0),
                    move_1 = poke_list.get('move_1',0),
                    move_2 = poke_list.get('move_2',0),
                    individual_attack = poke_list.get('individual_attack',0),
                    individual_defense = poke_list.get('individual_defense',0),
                    individual_stamina = poke_list.get('individual_stamina',0),
                    stamina_max = poke_list.get('stamina_max',0),
                    stamina = poke_list.get('stamina',0),
                    height_m = poke_list.get('height_m',0.0),
                    weight_kg = poke_list.get('weight_kg',0.0),
                    cp = poke_list.get('cp',0),
                    cp_multiplier = poke_list.get('cp_multiplier',0.0),
                )
                #Create Item Object
                item, created = InventoryItem.objects.get_or_create(
                    owner = profile,
                    poke_data = pokemon,
                )

            if 'item' in inventory_item['inventory_item_data']:

                itemdata, created = ItemData.objects.get_or_create(
                    item_id = inventory_item['inventory_item_data']['item'].get('item_id',0),
                )

                #Create Item Object
                item, created = InventoryItem.objects.get_or_create(
                    owner = profile,
                    item_data = itemdata,
                )
                item.count = inventory_item['inventory_item_data']['item'].get('count',0)
                item.save()

            if 'player_stats' in inventory_item['inventory_item_data']:
                experience = inventory_item['inventory_item_data']['player_stats'].get('experience', 0)
                print(experience)
                level = inventory_item['inventory_item_data']['player_stats'].get('level', 0)
                km_walked = inventory_item['inventory_item_data']['player_stats'].get('km_walked', 0.0)

                if not profile.statistics:
                    statistics, created = Statistics.objects.get_or_create(
                        experience = experience,
                        level = level,
                        km_walked = km_walked,
                    )
                    profile.statistics = statistics
                    profile.save()
                else:
                    profile.statistics.experience = experience
                    profile.statistics.level = level
                    profile.statistics.km_walked = km_walked
                    profile.statistics.save()

        return HttpResponse('ok')
