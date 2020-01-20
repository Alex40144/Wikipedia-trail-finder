import httplib2
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()



start = 'https://en.wikipedia.org/wiki/NASA'
target = 'https://en.wikipedia.org/wiki/Curiosity_(rover)'
StartPage = start[start.find('/wiki/'):]
TargetPage = target[target.find('/wiki/'):]
status, response = http.request(start)

def GetLinksFromPage(page):
    links = []
    page = 'https://en.wikipedia.org' + page
    status, response = http.request(page)
    for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            if link['href'][:6] == '/wiki/':
                print(link['href'])
                links.append(link['href'])
    return links



def loop(StartPage, TargetPage):
    pages = []
    print('Finding the shortest path between the %s and %s pages...' % (StartPage, TargetPage))
    pages.append(GetLinksFromPage(StartPage))
    for i in range (5):
        for page in pages[i]:
            pages.append(GetLinksFromPage(page))

    print(pages)








loop(StartPage, TargetPage)