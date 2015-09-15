# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Catalog_Scraper.items import catalogscraperItem
from scrapy.loader.processors import TakeFirst
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join
import re

class catalogsspider(CrawlSpider):
    name = 'catalog'
    allowed_domains = ['rainbowhistory.omeka.net']
    start_urls = ['http://rainbowhistory.omeka.net/items/show/4939296']
    rules = (
        # In the braces following "allow" provide the xpath shared by items in the catalog as follows: ""'your/x/path',". This instructs your scraper to follow links to catalog items and then perform parse_CatalogRecord on their contents.
        Rule(LinkExtractor(allow=('items/show/.*')),callback='parse_CatalogRecord',
#follow=True #this section can be comented out to limit my crawl to a single page. Removal of the comment mark allows it to crawl the entire site.
),)

# As the spider reaches pages identified through the LinkExtractor rule, it passes them to "parse_CatalogRecord". Rather than extracting data from every page however, "parse_CatalogRecord" attempts to collect information only from those pages determined to be relevent to the subject being researched, based on whether or not those pages contain one of the keywords included in the file "keys.txt". First, "keys.txt" is opened and its contents are strung into a regular expression. Each word in the regular expression is esperated by "|" which indicates "or", and enclosed in the tag "r"\b"", which clarifies that each piece of the expression is a complete word, not a character string. The resulting regular expression becomes the object "keywords". "keywords" is transformed into a pattern and stored for repeated use as "r". Finally, "parse_CatalogRecord" asks whether the webpage it has been passed contains one of the keywords from "keys.txt" by searching for the pattern stored in "r" within the "response.body_as_unicode". If one of the keywords appears, information is retrieved from the page and in a csv file. If no keyword can be found, that page is ignored and the the spider proceeds to the next.

    def parse_CatalogRecord(self, response):
        CatalogRecord = ItemLoader(item=catalogscraperItem(), response=response)
        CatalogRecord.default_output_processor = TakeFirst()
        keywords = '|'.join(r"\b" + re.escape(word.strip()) + r"\b" for word in open('Catalog_Scraper/spiders/keys.txt'))
        r = re.compile('.*(%s).*' % keywords, re.IGNORECASE|re.MULTILINE|re.UNICODE)
        if r.search(response.body_as_unicode()):
            # The following lines tell the spider how to populate the fields defined in "items.py". The first argument of "CatalogRecord.add_xpath" indicated which field the spider is being directed to fill, while the second provides an xpath, directing the spider to where the relevent information is contained on a give webpage.
            CatalogRecord.add_xpath('title', './/div[@id="dublin-core-title"]/div[@class="element-text"]/text()')
            # CatalogRecord.add_xpath('subject', '')
            # CatalogRecord.add_xpath('description', '')
            # CatalogRecord.add_xpath('creator', '')
            # CatalogRecord.add_xpath('source', '')
            # CatalogRecord.add_xpath('published', '')
            # CatalogRecord.add_xpath('published', '')
            # CatalogRecord.add_xpath('rights', '')
            # CatalogRecord.add_xpath('citation', '')
            # CatalogRecord.add_xpath('url', '')
            return CatalogRecord.load_item()
