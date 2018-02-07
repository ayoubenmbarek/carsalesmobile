# -*- coding: utf-8 -*-

# Scrapy settings for carsalesmobile project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'carsalesmobile'

SPIDER_MODULES = ['carsalesmobile.spiders']
NEWSPIDER_MODULE = 'carsalesmobile.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'carsalesmobile (+http://www.yourdomain.com)'
#USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
FEED_EXPORT_FIELDS = ['ANNONCE_LINK', 'ANNONCE_DATE', 'ID_CLIENT', 'GARAGE_ID', 'TYPE', 'SITE', 'MARQUE', 'MODELE', 'ANNEE', 'MOIS', 'NOM', 'CARROSSERIE', 'OPTIONS', 'CARBURANT', 'CYLINDRE', 'PUISSANCE', 'PORTE', 'BOITE', 'ENGINE', 'NB_VITESSE', 'PRIX', 'KM', 'PLACE', 'COULEUR', 'PHOTO', 'LITRE', 'TRANSMISSION', 'IMMAT', 'No_VEHICULE', 'VIN', 'VN_IND', 'CONTACT', 'LOCATION', 'CONTACT_PRENOM', 'CONTACT_NOM', 'GARAGE_NAME', 'ADRESSE', 'VILLE', 'CP', 'DEPARTEMENT', 'PROVINCE', 'TELEPHONE', 'TELEPHONE_2', 'TELEPHONE_3', 'TELEPHONE_4', 'TELEFAX', 'EMAIL', 'SIRET']
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
        'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
#    'carsalesmobile.middlewares.CarsalesmobileSpiderMiddleware': 543,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html

SPLASH_URL = 'http://0.0.0.0:8050'
DOWNLOADER_MIDDLEWARES = {

   # 'carsalesmobile.middlewares.MyCustomDownloaderMiddleware': 543,
   #'scrapy_splash.SplashCookiesMiddleware': 723,
    #'scrapy_splash.SplashMiddleware': 725,
    #'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
   #'carsalesmobile.rotate_useragent.RotateUserAgentMiddleware' :400,
     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
     #'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
     #'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
     #'scrapy.downloadermiddlewares.retry.RetryMiddleware': None, #changed 16/08
     #'carsalesmobile.middlewares.RetryMiddleware': 200,	
     #carsalesmobile.middlewares.ProxyMiddleware': 410,
     'carsalesmobile.middlewares.RandomUserAgentMiddleware': 400,
     #'carsalesmobile.middlewares.RetryChangeProxyMiddleware': 600, 
     #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,	
   
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
RETRY_TIMES = 10
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'carsalesmobile.pipelines.CarsalesmobilePipeline': 300,
#}
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
USER_AGENT_LIST = "/home/databiz41/useragents.txt"
HTTP_PROXY = 'http://127.0.0.1:8128'
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

