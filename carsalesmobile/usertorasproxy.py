def random_dedicate_proxy():
    dedicated_ips = [  proxy1, proxy2, proxy3
                ]
    dedicated_proxies = [{'http':'http://' + ip, 'https':'https://' + ip} for ip in dedicated_ips]
    return choice(dedicated_proxies)

def proxy_selector(url):
    TOR_CLIENT = 'socks5h://127.0.0.1:9050'
    if '.onion' in url:
        proxy  = {'http': TOR_CLIENT, 'https': TOR_CLIENT}
    else:
        proxy = random_dedicate_proxy()
    return proxy

def get_urls_from_spreadsheet():
    fname = 'list_of_stuff.csv'
    url_df = pd.read_csv(fname,usecols=['URL'],keep_default_na=False)
    URL = url_df.URL.dropna()
    urls = [clean_url(url) for url in URL if url != '']
    return urls

class BasicSpider(scrapy.Spider):

    name = "basic"
    rotate_user_agent = True
    start_urls = get_urls_from_spreadsheet()


    def parse(self, response):
        item = StatusCehckerItem()
        item['url'] = response.url
        item['status_code'] = response.status
        item['time'] = time.time()
        response.meta['proxy'] = proxy_selector(response.url)
        return item

class BasicSpider(scrapy.Spider):

    custom_settings = {
        'HTTPPROXY_ENABLED': True # can also set this in the settings.py file
    }
    name = "basic"
    rotate_user_agent = True

    def start_requests(self):
        urls = get_urls_from_spreadsheet()
        for url in urls:
            proxy = proxy_selector(url)
            yield scrapy.Request(url=url, callback=self.parse, meta={'proxy': proxy})

    def parse(self, response):
        item = StatusCehckerItem()
        item['url'] = response.url
        item['status_code'] = response.status
        item['time'] = time.time()
        return item

#crawlera and splash with scrapy  https://github.com/scrapy-plugins/scrapy-splash/issues/97
