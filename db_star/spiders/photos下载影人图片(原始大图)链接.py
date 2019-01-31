# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PhotosSpider(CrawlSpider):
    name = 'photos'
    allowed_domains = ["movie.douban.com", "img1.doubanio.com", "img2.doubanio.com",
                       "img3.doubanio.com", "img4.doubanio.com"]
    start_urls = ['http://movie.douban.com/celebrity/1000120/photos/']
    photo_links = LinkExtractor(allow="photo", tags="img", attrs="src", deny_extensions="")
    rules = (
        Rule(LinkExtractor(allow="sortby=like")),
        Rule(photo_links, process_links="parse_links")
    )

    def parse_links(self, links):
        filename = open("photo_links.txt", "a")
        for link in links:
            link.url = link.url.replace("/m/", "/raw/").replace("webp", "jpg")
            filename.write(link.url+"\n")
        filename.close()
        return links


