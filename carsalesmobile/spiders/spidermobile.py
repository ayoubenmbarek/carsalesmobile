# -*- coding: utf-8 -*-
import scrapy
import logging
import re
import json
import time
from scrapy.spiders import CrawlSpider
from scrapy.conf import settings
from ..items import CarsalesmobileItem
#try to use splash
class CarsalesMobileSpider(scrapy.Spider):
        name = "newcarsalesmobileafterlast"
        handle_httpstatus_list = [301, 302, 502]
        allowed_domains = ["carsales.mobi"]
	download_delay = 0
	start_urls = ['https://carsales.mobi/mobiapi/carsales/v2/stock/listing?p=Service.Carsales.&pg=1&sb=MakeModel&ni=60']
	#start_urls = ['https://carsales.mobi/cars/details/Mazda-3-2017/OAG-AD-15003515']
	
	
        def parse(self, response):	
                data = json.loads(response.body)
                headers = {
    		'Content-Type': 'json/...',
			}
                
                for jsonresponse in data.get('Result', []): 
                        myItem = CarsalesmobileItem()
                        myItem['ID_CLIENT'] = jsonresponse.get('NetworkId')
                        myItem['NOM'] = jsonresponse.get('DisplayTitle')
                        myItem["SELLER_TYPE"] = jsonresponse.get('SiloTypeFriendlyName') 
                        myItem['MARQUE'] = jsonresponse.get('KruxData', {})[0].get('Items')[3].get('Value')
                        myItem['MODELE'] = jsonresponse.get('KruxData', {})[0].get('Items')[4].get('Value')
                        myItem['COULEUR'] = jsonresponse.get('KruxData', {})[0].get('Items')[7].get('Value')
                        myItem['ANNEE'] = jsonresponse.get('KruxData', {})[0].get('Items')[8].get('Value')
                        myItem['CARBURANT'] = jsonresponse.get('KruxData', {})[0].get('Items')[11].get('Value')
                        try:
                            myItem['VN_IND'] = jsonresponse.get('KruxData', {})[0].get('Items')[12].get('Value')
                        except:
                            pass
                        myItem["PROVINCE"] = jsonresponse.get('DisplayLocation') 
                        myItem["PRIX"] = jsonresponse.get('DisplayPrice', {}).get('Price')
                        myItem["PHOTO"] = jsonresponse.get('MainPhoto')
                        myItem["KM"] = jsonresponse.get('KeyDetails')[0] 
                        myItem["BOITE"] = jsonresponse.get('KeyDetails')[2]
                        #myItem['DESCRIPTION'] = jsonresponse.get('Comment')
                        url = 'https://carsales.mobi/mobiapi/carsales/v3/stock/details/'
                        full_url = url + myItem['ID_CLIENT']
                        myItem['ANNONCE_LINK'] = full_url
                        try:
                                myItem["ENGINE"] = jsonresponse.get('KeyDetails')[3]
                        except:
                                pass
                        myItem["CARROSSERIE"] = jsonresponse.get('KeyDetails')[1]
			            #web_url = jsonresponse.get('WebDetailsUrl')
			            #base_url = 'https://carsales.mobi/'
			            #full_web_url = web_url + base_url
			            #myItem['ANNONCE_LINK'] = full_web_url
			
                        url = 'https://carsales.mobi/mobiapi/carsales/v3/stock/details/'
                        full_url = url + myItem['ID_CLIENT']
                        #myItem['ANNONCE_LINK'] = full_url
                        request = scrapy.Request(full_url, callback = self.adv_page)
                        request.meta["myItem"] = myItem
                        yield request
                for i in range(1,3795):#3794,
	                next_page = 'https://carsales.mobi/mobiapi/carsales/v2/stock/listing?p=Service.Carsales.&pg='+str(i)+'&sb=MakeModel&ni=60'
	                yield scrapy.Request(next_page)#, callback = self.parse)
                
        def adv_page(self, response):
            data = json.loads(response.body)
            myItem = response.meta['myItem']
            
                #for jsonresponse in data.get('Result', []):
            try:
                myItem['ANNONCE_DATE'] =  data.get('Result')[0].get('GaData').get('Items')[4].get('Value')
            except:
                pass
                
            try:
                myItem['GARAGE_ID'] =  data.get('Result')[0].get('Krux')[0].get('Items')[11].get('Value')   
            except:
                pass
                
            try:
                myItem['IMMAT'] =  data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[1].get('Items')[1].get('Value')
            except:
                pass
                
            try:
                myItem['TRANSMISSION'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[0].get('Items')[2].get('Value')
            except:
                pass
                
            try:
                myItem["CYLINDRE"] = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[1].get('Items')[5].get('Value')
            except:
                pass
                
            try:
                myItem['MOIS'] = data.get('Result')[0]('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[8].get('Items')[2].get('Value')
            except:
                pass
                
            try:
                myItem['GARAGE_NAME'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[6].get('Items')[0].get('Value')
            except:
                pass
                
            try:
                myItem['CONTACT_PRENOM'] = data.get('Result')[0].get('Enquiry').get('ContactName')
            except:
                pass
            try:
                myItem['PLACE'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[7].get('Items')[7].get('Value')
            except:
                pass
            try:
                myItem['DESCRIPTION'] = data.get('Result')[0].get('AppAnnotation').get('Description')
            except:
                pass
            #try:
            #except:
              #  pass
            try:
                myItem['PORTE'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[7].get('Items')[7].get('Value')
            except:
                pass
            
             
            
            
            
            
           # myItem['MARQUE'] =  data.get('Result')[0].get('GaData').get('Items')[2].get('Value')
            #myItem['MODELE'] =  data.get('Result')[0].get('GaData').get('Items')[3].get('Value')
            #myItem['ANNONCE_LINK'] = data.get('Result')[0].get('Share').get('WebUrl') 
            #myItem['ANNEE'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[8].get('Items')[1].get('Value')#The year in which this vehicle was first built
            try:
                cc =  data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[5].get('Items')[1].get('Value')
                cc2 = cc.split('|')
                myItem['TELEPHONE'] = cc2[0]
            except:
                pass
            #myItem['DATE_FABRICATION'] = jsonresponse.get('Sections')[2].get('Tabs')[0].get('Sections')[1].get('Items')[10].get('Value')#The date this actual car was built.
            
            
            #myItem["SELLER_TYPE"] = data.get('Result')[0].get('Krux')[0].get('Items')[12].get('Value')
            
            
            #myItem['VN_IND'] = data.get('Result')[0].get('GaData').get('Items')[6].get('Value')
            
            
            
            #myItem['COULEUR'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[1].get('Items')[2].get('Value')
            #couleur_interieur = data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[1].get('Items')[3].get('Value')
            try:
                myItem['LITRE'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[1].get('Items')[2].get('Value')
            except:
                pass
            
            try:
                myItem['COUNTRY'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[8].get('Items')[0].get('Value')
            except:
                pass#country of origin
            
            
            #myItem['CARBURANT'] = data.get('Result')[0].get('Krux')[0].get('Items')[10].get('Value')
        #except:
            #pass
            yield myItem
                        

