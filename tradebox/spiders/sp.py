import scrapy


class SpSpider(scrapy.Spider):
    name = "sp"
    allowed_domains = ["tradebox.shop"]
    start_urls = ["http://tradebox.shop/catalog/lcd"]
    page = 1

    def parse(self, response):
        for product in response.css('div.card'):
            print(product.css('a.card__title::text').get())
            yield {
                'name': product.css('a.card__title::text').get(),
                'link': response.urljoin(product.css('a.card__img::attr(href)').get()),
                'price': product.css('div.card__price::text').get(),
                'code': product.css('div.card__code strong::text').get(),
            }

        self.page += 1
        url = f'http://tradebox.shop/catalog/lcd?page={self.page}'
        if response.css('div.card'):
            yield response.follow(url, self.parse)
