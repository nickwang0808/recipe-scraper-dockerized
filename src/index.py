import sys
from recipe_scrapers import scrape_me
import json
from checkUrl import checkUrl


class Scraper:
    def __init__(self, url):
        wild_mode = checkUrl(url)
        print("using wild_mode", wild_mode)
        # todo: run regex to check if the input url is in the predefined supported sites
        result = scrape_me(url, wild_mode=wild_mode)

        self.title = result.title()
        self.total_time = result.total_time()
        self.yields = result.yields()
        self.ingredients = result.ingredients()
        self.instructions = result.instructions()
        self.image = result.image()
        # self.host = result.host()
        # self.links = result.links()
        # self.nutrients = result.nutrients()


url = sys.argv[1]
# wild_mode = sys.argv[2]
# result = Scraper(url, wild_mode)
result = Scraper(url)
print(json.dumps(vars(result)))
# print(json.dumps(vars(result), sort_keys=True, indent=4))
