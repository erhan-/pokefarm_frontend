from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import requests
import json
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.http import HttpResponseRedirect, Http404


# Models
from .models import Profile, InventoryItem, Pokemon, PokeData, ItemData, Statistics, Connection


# Views
def get_location(profile):
    url = 'http://'+profile.connection.hostname+':'+str(profile.connection.port)+'/position'
    try:
        location = requests.get(url).json()
    except:
        location = False
    return location


class Filldata(View):
    def get(self, request, *args, **kwargs):
        # item_json = 'https://raw.githubusercontent.com/PokemonGoF/PokemonGo-Bot/dev/data/items.json'
        # item_response = requests.get(item_json).json()
        # items_db = ItemData.objects.all()
        # for key, value in item_response.iteritems():
        #     item, created = ItemData.objects.get_or_create(
        #         item_id = key
        #     )
        #     item.name = value
        #     item.save()

        profi = 'https://raw.githubusercontent.com/PokemonGoF/PokemonGo-Bot/dev/data/pokemon.json'
        poke_response = requests.get(poke_json).json()
        poke_db = PokeData.objects.all()
        for poke in poke_response:
            pokedata, created = PokeData.objects.get_or_create(
                poke_id = poke['Number']
            )
            pokedata.name = poke['Name']
            pokedata.candy = poke.get('Amount', 0)
            pokedata.save()


        return HttpResponse('ok')

class ReleasePoke(View):
    def get(self, request, *args, **kwargs):

        poke = Pokemon.objects.get(individual_id=kwargs['poke_id'])
        return render(request, 'release_confirm.html', {'poke': poke})

    def post(self, request, *args, **kwargs):
        if "sure" not in request.POST:
            return HttpResponse("not sure")

        profile = Profile.objects.get(id=kwargs['account_id'])
        url = 'http://'+profile.connection.hostname+':'+str(profile.connection.port)+'/release'
        data = {'pokeid' : kwargs['poke_id'],}
        response = requests.post(url,data=data, auth=('admin', 'secret')).json()
        """
        UNSET = 0;
		SUCCESS = 1;
		POKEMON_DEPLOYED = 2;
		FAILED = 3;
        ERROR_POKEMON_IS_EGG = 4;
        """
        if 'result' not in response:
            return HttpResponse(response)
        if response['result'] == 1:
            poke = Pokemon.objects.get(individual_id=kwargs['poke_id']).delete()
            return HttpResponseRedirect('/list/2/')
        else:
            # Failed
            return HttpResponseRedirect('/list/2/')


class EvolvePoke(View):
    def get(self, request, *args, **kwargs):

        poke = Pokemon.objects.get(individual_id=kwargs['poke_id'])
        evolved_id = poke.pokemon_id+1
        evolved = PokeData.objects.get(poke_id=evolved_id)
        return render(request, 'evolve_confirm.html', {'poke': poke, 'evolved':evolved })

    def post(self, request, *args, **kwargs):
        if "sure" not in request.POST:
            return HttpResponse("not sure")
        poke = Pokemon.objects.get(individual_id=kwargs['poke_id'])
        profile = Profile.objects.get(id=kwargs['account_id'])
        url = 'http://'+profile.connection.hostname+':'+str(profile.connection.port)+'/evolve'
        data = {'pokeid' : kwargs['poke_id'],}
        response = requests.post(url,data=data, auth=('admin', 'secret')).json()
        """
		UNSET = 0;
		SUCCESS = 1;
		FAILED_POKEMON_MISSING = 2;
		FAILED_INSUFFICIENT_RESOURCES = 3;
		FAILED_POKEMON_CANNOT_EVOLVE = 4;
        FAILED_POKEMON_IS_DEPLOYED = 5;
        """
        print(response)
        if 'result' not in response:
            return HttpResponse(response)
        if response['result'] == 1:
            # Evolve Pokemon in Database
            evolved_id = poke.pokemon_id+1
            evolved = PokeData.objects.get(poke_id=evolved_id)
            poke.poke_data = evolved
            poke.save()
            return HttpResponseRedirect('/list/2/')

        else:
            print("Error %s",response['result'])
            return HttpResponseRedirect('/list/2/')




class PokeList(View):
    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, id=kwargs['account_id'])
        location = get_location(profile)
        inventory = InventoryItem.objects.filter(owner=profile).order_by('-count','-poke_data__cp')
        return render(request, 'poke_list.html', {'inventory_list': inventory, 'profile': profile, 'location': location })


class Sync(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(id=kwargs['account_id'])
        url = 'http://'+profile.connection.hostname+':'+str(profile.connection.port)+'/inventory'
        inventory_items = requests.get(url, auth=('admin', 'secret')).json()

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
