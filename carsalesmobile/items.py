# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarsalesmobileItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
        ANNONCE_LINK = scrapy.Field()
        VIN = scrapy.Field()
        ANNONCE_DATE = scrapy.Field()
        ID_CLIENT = scrapy.Field()
        LOCATION = scrapy.Field()
        GARAGE_ID = scrapy.Field()
        ENGINE = scrapy.Field()
        TYPE = scrapy.Field()
        SITE = scrapy.Field()
	SELLER_TYPE = scrapy.Field()
        TRANSMISSION = scrapy.Field()
        #DATE_FABRICATION = scrapy.Field()
        DESCRIPTION = scrapy.Field()
        MARQUE = scrapy.Field()
        MODELE = scrapy.Field()
        ANNEE = scrapy.Field()
        MOIS = scrapy.Field()
        NOM = scrapy.Field()
        CARROSSERIE = scrapy.Field()
        OPTIONS = scrapy.Field()
        CARBURANT = scrapy.Field()
        CYLINDRE =scrapy.Field()
        PUISSANCE = scrapy.Field()
        PORTE = scrapy.Field()
        BOITE = scrapy.Field()
        NB_VITESSE = scrapy.Field()
        PRIX = scrapy.Field()
        KM = scrapy.Field()
        PLACE = scrapy.Field()
        COULEUR = scrapy.Field()
        PHOTO = scrapy.Field(serializer=str)
        LITRE = scrapy.Field()
        IMMAT = scrapy.Field()
        No_CHASSIS = scrapy.Field()
        VN_IND = scrapy.Field()
        CONTACT = scrapy.Field()
        CONTACT_PRENOM = scrapy.Field()
        CONTACT_NOM = scrapy.Field()
        GARAGE_NAME = scrapy.Field()
        ADRESSE = scrapy.Field()
        VILLE = scrapy.Field()
        CP = scrapy.Field()
        DEPARTEMENT = scrapy.Field()
        PROVINCE = scrapy.Field()
        COUNTRY = scrapy.Field()
        TELEPHONE = scrapy.Field()
        TELEPHONE_2 = scrapy.Field()
        TELEPHONE_3 = scrapy.Field()
        TELEPHONE_4 = scrapy.Field()
        TELEFAX = scrapy.Field()
        EMAIL = scrapy.Field()
        SIRET = scrapy.Field()
        No_VEHICULE = scrapy.Field()
        #pass
