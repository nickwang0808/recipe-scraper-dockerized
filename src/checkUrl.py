import re

siteList = """https://www.750g.com
https://claudia.abril.com.br/
https://www.acouplecooks.com
https://allrecipes.com/
https://amazingribs.com/
https://ambitiouskitchen.com/
https://archanaskitchen.com/
https://www.atelierdeschefs.fr/
https://averiecooks.com/
https://bakingmischief.com/
https://bbc.com/
https://bbc.co.uk/
https://bbcgoodfood.com/
https://bettycrocker.com/
https://blueapron.com/
https://bonappetit.com/
https://bowlofdelicious.com/
https://budgetbytes.com/
https://cdkitchen.com/
https://chefkoch.de/
https://closetcooking.com/
https://cookeatshare.com/
https://cookieandkate.com/
https://cookpad.com/
https://cookstr.com/
https://copykat.com/
https://countryliving.com/
https://cuisineaz.com/
https://cybercook.com.br/
https://delish.com/
https://domesticate-me.com/
https://downshiftology.com/
https://www.dr.dk/
https://www.eatingbirdfood.com/
https://eatsmarter.com/
https://eatsmarter.de/
https://eatwhattonight.com/
https://epicurious.com/
https://recipes.farmhousedelivery.com/
https://fifteenspatulas.com/
https://finedininglovers.com/
https://fitmencook.com/
https://food.com/
https://foodandwine.com/
https://foodnetwork.com/
https://foodrepublic.com/
https://geniuskitchen.com/
https://giallozafferano.it/
https://gimmesomeoven.com/
https://recietas.globo.com/
https://gonnawantseconds.com/
https://gousto.co.uk/
https://greatbritishchefs.com/
https://halfbakedharvest.com/
https://www.hassanchef.com/
https://www.heb.com/
https://heinzbrasil.com.br/
https://hellofresh.com/
https://hellofresh.co.uk/
https://www.hellofresh.de/
https://hostthetoast.com/
https://101cookbooks.com/
https://receitas.ig.com.br/
https://inspiralized.com/
https://jamieoliver.com/
https://justbento.com/
https://kennymcgovern.com/
https://www.kingarthurbaking.com
https://kochbar.de/
https://kuchnia-domowa.pl/
https://littlespicejar.com/
http://livelytable.com/
https://lovingitvegan.com/
https://lecremedelacrumb.com/
https://marmiton.org/
https://matprat.no/
http://mindmegette.hu/
https://minimalistbaker.com/
https://misya.info/
https://momswithcrockpots.com/
http://motherthyme.com/
https://mybakingaddiction.com/
https://myrecipes.com/
https://healthyeating.nhlbi.nih.gov/
https://nourishedbynutrition.com/
https://nutritionbynathalie.com/blog
https://cooking.nytimes.com/
https://ohsheglows.com/
https://www.paleorunningmomma.com/
https://www.panelinha.com.br/
https://paninihappy.com/
https://popsugar.com/
https://przepisy.pl/
https://purelypope.com/
https://purplecarrot.com/
https://rachlmansfield.com/
https://realsimple.com/
https://recipietineats.com/
https://seriouseats.com/
https://simplyquinoa.com/
https://simplyrecipes.com/
https://simplywhisked.com/
https://skinnytaste.com/
https://southernliving.com/
https://spendwithpennies.com/
https://www.thespruceeats.com/
https://steamykitchen.com/
https://streetkitchen.hu/
https://sunbasket.com/
https://sweetpeasandsaffron.com/
https://tastesoflizzyt.com
https://tasteofhome.com
https://tasty.co
https://tastykitchen.com/
https://thehappyfoodie.co.uk/
https://thekitchn.com/
https://thenutritiouskitchen.co/
https://thepioneerwoman.com/
https://thespruceeats.com/
https://thevintagemixer.com/
https://thewoksoflife.com/
https://tine.no/
https://tudogostoso.com.br/
https://twopeasandtheirpod.com/
https://vegolosi.it/
https://watchwhatueat.com/
https://whatsgabycooking.com/
https://en.wikibooks.org/
https://yummly.com/"""


def checkUrl(url):
    if url == None:
        return False
    sites = siteList.split("\n")
    trimmed = list(map(lambda s: s.replace("https://", ""), sites))

    regex = "|".join(trimmed)

    result = not bool(re.search(regex, url))
    return result


checkUrl("dwa")
