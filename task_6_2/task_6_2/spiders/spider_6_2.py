import scrapy
"""to use scrapy.Spider"""

n = 1000
# number of games

# scrapy crawl spider -o gamestages.csv -t csv
# to get result in gamestages.csv


class Steam_Games_Spider(scrapy.Spider):
    name = 'spider'
    url = 'https://store.steampowered.com/search/?category1=998&filter=topsellers&ndl=1&page=%s'
    # top-selled games in Steam
    page = 1
    start_urls = [url % page]
    # changing the page
    count = 0

    def parse(self, response):
        """get games' links"""
        global n
        for obj in response.css('a.search_result_row.ds_collapse_flag'):  # link to every game
            yield response.follow(obj, callback=self.tags)  # go to game page
        if self.count < n:
            self.page += 1
            yield response.follow(self.url % self.page, callback=self.parse)
            # go to next page

    def tags(self, response):
        """get tags"""
        global n
        name = response.css("div.apphub_AppName::text").get()  # game name
        if self.count == n:  # got 1000
            return
        self.count += 1
        yield {
            'name': name,
            'tags': list(map(str.strip, response.css('a.app_tag::text').getall()))  # all game tags
        }
