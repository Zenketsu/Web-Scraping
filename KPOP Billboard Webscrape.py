import requests
from bs4 import BeautifulSoup

url = "https://www.billboard.com/charts/billboard-korea-k-pop-100/2018-05-05"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

links = soup.find_all("a")

for link in links:
    print ""