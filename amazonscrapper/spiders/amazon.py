import scrapy
import time
class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.in/s?k=book&crid=398S68NEU4EIS&sprefix=book%2Caps%2C244&ref=nb_sb_noss_1']

    def parse(self, response):
        # Extracting product listings
        product_listings = response.xpath('//div[@data-component-type="s-search-result"]')

        for product in product_listings:
            # Extracting product title
            title = product.xpath(".//span[@class='a-size-medium a-color-base a-text-normal']/text()").get()

            # Extracting product price
            price = product.xpath(".//span[@class='a-price-whole']/text()").get()

            # Extracting product URL
            url = product.xpath('.//h2/a/@href').get()
            if url:
                url = response.urljoin(url)

            # Extracting product reviews count
            reviews = product.xpath('.//span[contains(@class, "a-size-base") and contains(@class, "s-underline-text")]/text()').get()

            yield {
                'title': title,
                'price': price,
                'url': url,
                'reviews': reviews
            }

        # Follow pagination link
        time.sleep(5)
        next_page = response.xpath('//div[@class="a-section a-text-center s-pagination-container"]//a[3]/@href')
        if next_page:
            next_page = response.urljoin(next_page.get())
            
            yield scrapy.Request(next_page, callback=self.parse)
