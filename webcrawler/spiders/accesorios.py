# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from webcrawler.items import WebcrawlerItem
from bs4 import BeautifulSoup


class ElectronicsSpider(CrawlSpider):
    name = "accesorios"
    allowed_domains = [
    	"celulares.mercadolibre.com.ar",
    	"articulo.mercadolibre.com.ar"
    ]
    start_urls = [
        'https://celulares.mercadolibre.com.ar/accesorios/',
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pagination__next',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        soup = BeautifulSoup(response.body)
        item_links = soup.findAll("a", {"class":"item__info-title"})

        for b in item_links:
           link = b.get('href')
           yield scrapy.Request(link, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
    	soup = BeautifulSoup(response.body)
    	titleContainer = soup.findAll("h1", {"class":"item-title__primary"})
    	title = titleContainer[0].text.strip()
    	priceContainer = soup.findAll("span", {"class":"price-tag-fraction"})
    	price = priceContainer[0].text.strip()

    	item = WebcrawlerItem()
    	item['title'] = title
    	item['price'] = price
    	item['url'] = response.url
    	yield item