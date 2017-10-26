# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Daily(models.Model):
    sto = models.CharField(max_length=96, blank=True, null=True)
    cislo = models.CharField(max_length=10, blank=True, null=True)
    firma = models.CharField(max_length=30, blank=True, null=True)
    typ = models.CharField(max_length=25, blank=True, null=True)
    meridlo = models.CharField(max_length=43, blank=True, null=True)
    sn = models.CharField(max_length=9, blank=True, null=True)
    datum = models.DateTimeField(blank=True, null=True)
    stav = models.CharField(max_length=11, blank=True, null=True)
    jednotka = models.CharField(max_length=3, blank=True, null=True)
    posledni_odecet = models.CharField(db_column='posledni odecet', max_length=19, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    posledni_stav = models.CharField(db_column='posledni stav', max_length=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    jednotka_2 = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily'
