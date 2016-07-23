from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import requests
import json

# Create your views here.


class PokeList(View):
    def get(self, request, *args, **kwargs):
        inventory_items = requests.get('http://localhost:5008/inventory').json()
        pokemon_list = []
        player_stats = []
        items_list = []
        for inventory_item in inventory_items:
            if "pokemon_data" in inventory_item['inventory_item_data']:
                pokemon_list.append(inventory_item['inventory_item_data']['pokemon_data'])

            if 'player_stats' in inventory_item['inventory_item_data']:
                player_stats.append(inventory_item['inventory_item_data']['player_stats'])
            if 'item' in inventory_item['inventory_item_data']:
                items_list.append(inventory_item['inventory_item_data']['item'])
        return render(request, 'poke_list.html', {'pokemon_list': pokemon_list, 'items_list': items_list, 'player_stats': player_stats })
