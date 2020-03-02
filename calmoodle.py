import logging
import scrapy

#logging.getLogger('scrapy').setLevel(logging.WARNING)

class CalSpider(scrapy.Spider):
    name ="cal_spider"

    custom_settings = {
        'FEED_EXPORT_ENCODING': "utf-8",
    }

    start_urls = [f"https://www.moodle.aau.dk/calmoodle/public/?sid={id}" for id in range(5789, 5790)]

    def parse(self, response):
        print("".join(response.css("title")[2].css("::text").extract()))
        # CONTENT_SELECTOR = "title"
        # for content in response.css(CONTENT_SELECTOR):
            
        #     NAME_SELECTOR = "b ::text"
        #     CN_SELECTOR = '//*[@id="mw-content-text"]/h2[span/text()="In other languages"]/following-sibling::table[@class="roundy"]/tr[1]/td/table/tr[td/a/span/text()="Mandarin Chinese"]/td[3]'
        #     yield {
        #         "name": content.css(NAME_SELECTOR).extract_first(),
        #         "cn": content.xpath(CN_SELECTOR).extract(),
        #     }