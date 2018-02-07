# -*- coding: utf-8 -*-
import scrapy
import logging
import re
import json
import time
from scrapy.spiders import CrawlSpider
from scrapy.conf import settings
from ..items import CarsalesmobileItem
from scrapy_splash import SplashRequest
#try to use splash
class CarsalesMobileSpider(scrapy.Spider):
        name = "spidermobile05-02-18"###spidermobile03-01-18##    the hole last cache under spidermobile3 #old cache in spider mobile4
        handle_httpstatus_list = [301, 302, 502, 200]
        allowed_domains = ["carsales.mobi"]
	download_delay = 0
	download_timeout = 280
	start_urls = ['https://carsales.mobi/mobiapi/carsales/v2/stock/listing?p=Service.Carsales.&pg=1&sb=MakeModel&ni=60']
	#start_urls = ['https://carsales.mobi/cars/details/Mazda-3-2017/OAG-AD-15003515']
	#start_urls = ['https://carsales.mobi/mobiapi/carsales/v2/stock/listing?p=Service.Carsales.&pg=18&ni=60']
	
	
        def parse(self, response):	
                data = json.loads(response.body)
                #headers = {
    		#'Content-Type': 'json/...',
		#}
		headers = {
		
		        ':authority':'carsales.mobi',
                        ':method':'GET',
                       # ':path':'/mobiapi/carsales/v2/stock/listing?pg=1&ni=18',
                        ':scheme':'https',
                        'accept':'*/*',
                        'accept-encoding':'gzip, deflate, sdch, br',
                        'accept-language':'fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4',
                        'authorization':'Basic d2luYXBwOndpbmFwcDEyMw==',
                        #'cache-control':'no-cache',
                        'content-type':'application/json',
                       # 'cookie':'ak_bmsc=A593C9096C4E64DAAA517794C5B7B1F50210A25F3D4300009CB6D359DF9D7D53~pljrJLZy5AP7olCHnd7B/i1p9lTMQH4QtVlv1hIi5KSn3vqTdViXSTh0fqbPoLX079tZEOmAjEdmrydoLqjwPWzufbHPape2721y150bk8rBSK3rKZjDKesq8xXslsnsPj9cKs7EP6zSQXvvPM4Y/XjxTpM1BMS9qEoiOqPtG/JiC3WD9h6ZLz1in8WkABlauL9U2fCRG8Jq/5D/bk+Hf1xLraqupMuKbJOIlBIpaZtnVWOtU2wgEp87px4XW80WJfBYtGdQKxYU9zNA3ZW1Ipdw==; __csnMobiExp__smartsearch_5_new=Default; _ga=GA1.2.2049612815.1507049770; _gid=GA1.2.949223249.1507049770; gaclientId=2049612815.1507049770; _gat=1; _gali=Refinement%2CSearch',
                        'pragma':'no-cache',
                        'referer':'https://carsales.mobi/cars/results',
                        'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36',
		                        }
		
                for jsonresponse in data.get('Result', []): 
                        myItem = CarsalesmobileItem()
                        myItem['ID_CLIENT'] = jsonresponse.get('NetworkId')
                        if 'SSE-AD' in myItem['ID_CLIENT']:
                                myItem['TYPE'] = 'Private'
                        else:
                                myItem['TYPE'] = 'Dealer'
                        km = jsonresponse.get('KeyDetails')[0] 
                        km1 = km.split('km')
                        km2 = km1[0]#myItem["KM"]
                        km2 = km2.replace(',','')
                        #km2 = km2.replace('$','')
                        if 'SHRM-AD' in myItem['ID_CLIENT']:
                                myItem["KM"] = 0
                        else:
                                myItem["KM"] = km2
                        myItem['SITE'] = 'carsales'
                        myItem['NOM'] = jsonresponse.get('DisplayTitle')
                        #myItem["SELLER_TYPE"] = jsonresponse.get('SiloTypeFriendlyName') 
                        seller_type = jsonresponse.get('SiloTypeFriendlyName')
			if  seller_type == 'Dealer Demo': 
			        myItem['VN_IND'] = 2
		        elif seller_type == 'Private':
		                myItem['VN_IND'] = 0
	                elif seller_type == 'Dealer Used':
		                myItem['VN_IND'] = 0
	                elif seller_type == 'New Car':
	                        myItem['VN_IND'] = 1
                        elif seller_type == 'Dealer New':
                                myItem['VN_IND'] = 1
                        myItem['MARQUE'] = jsonresponse.get('KruxData', {})[0].get('Items')[3].get('Value')
                        myItem['MODELE'] = jsonresponse.get('KruxData', {})[0].get('Items')[4].get('Value')
                        myItem['COULEUR'] = jsonresponse.get('KruxData', {})[0].get('Items')[7].get('Value')
                        myItem['ANNEE'] = jsonresponse.get('KruxData', {})[0].get('Items')[8].get('Value')
                        if len(myItem['ANNEE']) > 4:
                                myItem['ANNEE'] = 0

                        try:
                                myItem['CARBURANT'] = jsonresponse.get('KruxData', {})[0].get('Items')[11].get('Value')
                        except:
                                pass
                        #try:
                    	#	VN_IND = jsonresponse.get('KruxData', {})[0].get('Items')[12].get('Value')
                    		#if VN_IND == 'Used':
                    		#	myItem['VN_IND'] == 'Used'
            			#elif VN_IND == 'BNCIS':
            			#	myItem['VN_IND'] == 'New'
    				#elif VN_IND == 'Demo':
    				#	myItem['VN_IND'] =='Demo'
				#elif VN_IND == 'BNCA':
				#	myItem['VN_IND'] =='New'
				#elif VN_IND == 'Private':
				#	myItem['VN_IND'] =='Used'
                        #except:
                         #  pass
                        try:
                        	cc = jsonresponse.get('DisplayLocation')
                        	cc1 = ',' + cc
                        	cc2 = cc1.split(',')
                        	myItem["PROVINCE"] = cc2[-1]
                	except:
                		pass
                        prix = jsonresponse.get('DisplayPrice', {}).get('Price')
                        prix = prix.replace(',','')
                        prix = prix.replace('$','')
                        myItem["PRIX"] = prix
                        
                        try:
                                myItem["BOITE"] = jsonresponse.get('KeyDetails')[2]
                        except:
                                pass
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
                        request = scrapy.Request(full_url, headers=headers, callback = self.adv_page)
                        request.meta["myItem"] = myItem
                        yield request
                for i in range(2,3672):#3569 on january2018 #ancien 14/09 3795,i've started from 150 04/09  04/10 start from page3 #all 3717
                        #next_page = 'https://carsales.mobi/mobiapi/carsales/v2/stock/listing?p=Service.Carsales.&pg='+str(i)+'&ni=60'
	                next_page = 'https://carsales.mobi/mobiapi/carsales/v2/stock/listing?p=Service.Carsales.&pg='+str(i)+'&sb=MakeModel&ni=60'
	                yield scrapy.Request(next_page, headers=headers)#, callback = self.parse)
                
        def adv_page(self, response):
            data = json.loads(response.body)
            myItem = response.meta['myItem']
            
                #for jsonresponse in data.get('Result', []):
            try:
                myItem['ANNONCE_DATE'] =  data.get('Result')[0].get('GaData').get('Items')[4].get('Value')
            except:
                pass
            key = ' '
            key1 = ' '
            key2 = ' '
            try:
	        key = data.get('Result')[0].get('Sections')[1].get('Tags')[18].get('Key')
            except:
            	pass
	    try:
	        key1 = data.get('Result')[0].get('Sections')[1].get('Tags')[20].get('Key')
	    except:
	        pass
	    try:
	        key2 = data.get('Result')[0].get('Sections')[1].get('Tags')[19].get('Key')
	    except:
	        pass        
	    
	    if key == 'lmct':
		myItem['SIRET'] = data.get('Result')[0].get('Sections')[1].get('Tags')[18].get('Value')
	    elif key1 == 'lmct':
		myItem['SIRET'] = data.get('Result')[0].get('Sections')[1].get('Tags')[20].get('Value')
	    elif key2 == 'lmct':
	        myItem['SIRET'] = data.get('Result')[0].get('Sections')[1].get('Tags')[19].get('Value')
            else:
	        myItem['SIRET'] = ' '
				
            #except:
            	#pass
    	    try:
    	        myItem["PHOTO"] = len(data.get('Result')[0].get('Media').get('Photos'))
    	    except:
    	        pass
            try:
                garage_id =  data.get('Result')[0].get('Krux')[0].get('Items')[11].get('Value')
                garage_id2 = garage_id.split('-')                   
                myItem['GARAGE_ID'] = garage_id2[-1]
            except:
                pass
                
            try:
            	label = data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[1].get('Items')[1].get('Label')
            	if label == 'Reg Plate':
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
            	seat = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[8].get('Items')[7].get('Label')
            	if seat == 'Seat Capacity':
                	myItem['PLACE'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[8].get('Items')[7].get('Value')
		
            except:
                pass
            try:
                myItem['OPTIONS'] = data.get('Result')[0].get('AppAnnotation').get('Description')
            except:
                pass
            try:
            	label_door = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[8].get('Items')[6].get('Label')
            except:
                pass
            try:
            	label_door1 = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[8].get('Items')[7].get('Label')
            except:
            	pass
            try:
            	#label_door = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[8].get('Items')[6].get('Label')
            	#label_door1 = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[8].get('Items')[7].get('Label')
            	if label_door == 'Doors':
    			myItem['PORTE'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[8].get('Items')[6].get('Value')
            		

               #myItem['PORTE'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[7].get('Items')[7].get('Value')	
               
                elif label_door1 == 'Doors':
       	       		myItem['PORTE'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[8].get('Items')[7].get('Value')
            except:
                pass
            
             
            
            
            
            
           # myItem['MARQUE'] =  data.get('Result')[0].get('GaData').get('Items')[2].get('Value')
            #myItem['MODELE'] =  data.get('Result')[0].get('GaData').get('Items')[3].get('Value')
            #myItem['ANNONCE_LINK'] = data.get('Result')[0].get('Share').get('WebUrl') 
            #myItem['ANNEE'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[8].get('Items')[1].get('Value')#The year in which this vehicle was first built
            try:
            	myItem['TELEPHONE'] = data.get('Result')[0].get('Enquiry').get('NumberForDisplay')
                #cc =  data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[5].get('Items')[1].get('Value')
                #cc2 = cc.split('|')
                #myItem['TELEPHONE'] = cc2[0]
            except:
                pass
            #myItem['DATE_FABRICATION'] = jsonresponse.get('Sections')[2].get('Tabs')[0].get('Sections')[1].get('Items')[10].get('Value')#The date this actual car was built.
            
            
            #myItem["SELLER_TYPE"] = data.get('Result')[0].get('Krux')[0].get('Items')[12].get('Value')
            
            
            #myItem['VN_IND'] = data.get('Result')[0].get('GaData').get('Items')[6].get('Value')
            
            
            
            #myItem['COULEUR'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[1].get('Items')[2].get('Value')
            #couleur_interieur = data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[1].get('Items')[3].get('Value')
            try:
            	vin = data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[1].get('Items')[1].get('Label')
            	if vin == 'VIN':
            		myItem['VIN'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[1].get('Items')[1].get('Value')
            except:
            	pass
            try:
            	label = data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[1].get('Items')[9].get('Label')
            	label1 = data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[1].get('Items')[11].get('Label')
            	if label == 'Stock#':
            		myItem['No_VEHICULE'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[1].get('Items')[9].get('Value')
    		elif label1 == 'Stock#':
    			myItem['No_VEHICULE'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[0].get('Sections')[1].get('Items')[11].get('Value')
    			
            except:
            	pass		
            try:
                myItem['LITRE'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[1].get('Items')[2].get('Value')
            except:
                pass
            
            #try:
             #   myItem['COUNTRY'] = data.get('Result')[0].get('Sections')[2].get('Tabs')[2].get('Sections')[0].get('Groups')[0].get('Sections')[8].get('Items')[0].get('Value')
            #except:
                pass#country of origin
            
            
            #myItem['CARBURANT'] = data.get('Result')[0].get('Krux')[0].get('Items')[10].get('Value')
        #except:
            #pass
            yield myItem
                        

