import logging
import scrapy

#logging.getLogger('scrapy').setLevel(logging.WARNING)

with open('pkm') as f:
    pknames = [line.rstrip() for line in f]

class BulbaSpider(scrapy.Spider):
    name ="bulba_spider"

    custom_settings = {
        'FEED_EXPORT_ENCODING': "utf-8",
    }

    start_urls = [f"https://bulbapedia.bulbagarden.net/wiki/{mon}_(Pok%C3%A9mon)" for mon in pknames]

    def parse(self, response):
        #print("".join(response.css("div#mw-content-text>table")[0].css("::text").extract()))
        CONTENT_SELECTOR = "div#mw-content-text"
        for content in response.css(CONTENT_SELECTOR):
            
            NAME_SELECTOR = "b ::text"
            CN_SELECTOR = '//*[@id="mw-content-text"]/h2[span/text()="In other languages"]/following-sibling::table[@class="roundy"]/tr[1]/td/table/tr[td/a/span/text()="Mandarin Chinese"]/td[2]'
            DESC_SELECTOR = '//*[@id="mw-content-text"]/h2[span/text()="In other languages"]/following-sibling::table[@class="roundy"]/tr[1]/td/table/tr[td/a/span/text()="Mandarin Chinese"]/td[3]'
            yield {
                "name": content.css(NAME_SELECTOR).extract_first(),
                "cn": content.xpath(CN_SELECTOR).extract(),
                "desc": content.xpath(DESC_SELECTOR).extract(),
            }