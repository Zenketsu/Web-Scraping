import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import ExcelWriter
import datetime


def main():
    date = datetime.date(2018, 5, 19)
    print(date)
    webscrape(date)



def webscrape(date):

    date = date
    # get url data
    url = "https://www.billboard.com/charts/billboard-korea-k-pop-100/" + date.isoformat()
    r = requests.get(url)

    # parse url information
    soup = BeautifulSoup(r.content, "html.parser")

    # lists for Panda DataFrame
    peakPosition = []
    top100 = []
    currRank = []
    pastRank = []
    artist = []
    title = []

    # further narrow data down
    g_data = soup.find_all("div", {"class": "chart-row__secondary"})

    for item in g_data:
        # print out peak position
        # print "Peak Position"
        peakPosition.append(item.contents[1].find_all("div", {"class": "chart-row__top-spot"})[0].text[15:])

        # print out number of weeks on chart
        # print "Number of Weeks in Top 100"
        top100.append(item.contents[1].find_all("div", {"class": "chart-row__weeks-on-chart"})[0].text[14:])

    # new search in data
    g_data = soup.find_all("div", {"class": "chart-row__main-display"})

    for item in g_data:
        # prints out rank and previous week's rank
        # print "This week's ranking"
        currRank.append(item.contents[1].find_all("span", {"class": "chart-row__current-week"})[0].text)
        # print "Last week's ranking"
        pastRank.append(item.contents[1].find_all("span", {"class": "chart-row__last-week"})[0].text[11:])

        # prints out the artist
        # print "Artist"
        # different format for artist names in code
        # some of the artists' names are hyperlinked
        # try unlinked case
        try:
            artist.append(item.contents[5].find_all("span", {"class": "chart-row__artist"})[0].text[1:-1])
        # artist name is hyperlinked
        except:
            artist.append(item.contents[5].find_all("a", {"class": "chart-row__artist"})[0].text[1:-1])

        # prints out the song title
        # print "Song Title"
        title.append(item.contents[5].find_all("h2", {"class": "chart-row__song"})[0].text)

    # Create a Pandas dataframe from the data.
    df = pd.DataFrame(
        {"Current Ranking": currRank, "Last Week's Ranking": pastRank, "Song Title": title, "Artist": artist,
         "Peak Position": peakPosition, "Num Weeks in TOP 100": top100})

    df.to_csv(date.isoformat() + ' Billboard Kpop Rankings.csv', sep=',')




main()
