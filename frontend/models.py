from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    gauth = models.BooleanField(default=False)
    ptc = models.BooleanField(default=False)

class Connection(models.Model):
    hostname = models.CharField(max_length=40)
    port = models.IntegerField()
    token = models.CharField(max_length=40)

class Statistics(models.Model):
    experience = models.IntegerField()
    level = models.IntegerField()
    km_walked = models.FloatField()

class Profile(models.Model):
    player_name = models.CharField(max_length=40)
    account = models.ForeignKey(Account)
    connection = models.ForeignKey(Connection)
    statistics = models.ForeignKey(Statistics)
    loc_latitude = models.FloatField(default=0.0)
    loc_longitude = models.FloatField(default=0.0)
    min_cp = models.IntegerField(default=0)

class Eggs(models.Model):
    km = models.IntegerField()
    km2go = models.FloatField()


class PokeData(models.Model):
    name = models.CharField(max_length=42,default='Missingno')
    poke_id = models.IntegerField(blank=True,default=0)
    base_stamina = models.IntegerField(blank=True,default=0)
    base_attack = models.IntegerField(blank=True,default=0)
    base_defense = models.IntegerField(blank=True,default=0)
    type1 = models.IntegerField(blank=True,default=0)
    type2 = models.IntegerField(blank=True,default=0)
    base_capture_rate = models.FloatField(blank=True,default=0.0)
    base_flee_rate = models.FloatField(blank=True,default=0.0)
    evolution = models.IntegerField(blank=True,default=0)
    candy = models.IntegerField(blank=True,default=0)
    picture = models.ImageField(blank=True,upload_to='pokeimg/')

class Pokemon(models.Model):
    individual_id = models.CharField(max_length=64)
    poke_data = models.ForeignKey(PokeData)
    pokemon_id = models.IntegerField()
    move_1 = models.IntegerField()
    move_2 = models.IntegerField()
    individual_attack = models.IntegerField()
    individual_defense = models.IntegerField()
    individual_stamina = models.IntegerField()
    stamina_max = models.IntegerField()
    stamina = models.IntegerField()
    height_m = models.FloatField()
    weight_kg = models.FloatField()
    cp = models.IntegerField()
    cp_multiplier = models.FloatField()


class ItemData(models.Model):
    name = models.CharField(max_length=42,default='Unnamed')
    item_id = models.IntegerField()

class InventoryItem(models.Model):
    owner = models.ForeignKey(Profile)
    item_data = models.ForeignKey(ItemData, null=True)
    poke_data = models.ForeignKey(Pokemon, null=True)
    count = models.IntegerField(default=0)

    def delete(self, using=None):
        # BUG! Does not delete the objects from foreign key
        if self.poke_data:
            self.poke_data.delete()
        if self.item_data:
            self.item_data.delete()
        super(Profile, self).delete(using)
