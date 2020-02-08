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
    for link in BeautifulSoup(response, parse_only=SoupStrainer('mw-body-content'), features="html.parser"):
        if link.has_attr('href'):
            if link['href'][:6] == '/wiki/':
                links.append(link['href'])
    return links



def loop(StartPage, TargetPage):
    pages = []
    print('Finding the shortest path between the %s and %s pages...' % (StartPage, TargetPage))
    pages.append(GetLinksFromPage(StartPage))
    print(pages)
    print(TargetPage)
    if TargetPage in pages:
        print('page found after _ moves')








loop(StartPage, TargetPage)