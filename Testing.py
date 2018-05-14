import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Austin%2C+TX"
    r = requests.get(url)
    soup = BeautifulSoup(r.content)

    g_data = soup.find_all("div", {"class": "info"})

    for item in g_data:
        #prints out business name
        print item.contents[0].find_all("a", {"class": "business-name"})[0].text

        try:
            #prints out address, city, state, # zip code
            print item.contents[1].find_all("span", {"class": "street-address"})[0].text
            print item.contents[1].find_all("span", {"class": "locality"})[0].text.replace(',', '')
            print item.contents[1].find_all("span", {"itemprop": "addressRegion"})[0].text
            print item.contents[1].find_all("span", {"itemprop": "postalCode"})[0].text
        except:
            pass

        try:
            #prints out phone number
            print item.contents[1].find_all("div", {"class": "phones phone primary"})[0].text
        except:
            pass



main()
