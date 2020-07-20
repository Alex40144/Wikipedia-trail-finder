import urllib.request
from bs4 import BeautifulSoup, SoupStrainer

#TODO change to usesr input
start = input("URL of starting page: ")
target = input("URL of Ending page: ")

max_attempts = 4


StartPage = start[start.find('/wiki/'):]
TargetPage = target[target.find('/wiki/'):]


class WTF:
    def __init__(self, StartPage, TargetPage, max_attempts):
        self.StartPage = StartPage
        self.TargetPage = TargetPage
        self.max_attempts = max_attempts
        self.paths = {StartPage:[StartPage]}
        self.queue = [StartPage]
        self.attempts = 0

    def GetLinksFromPage(self, page):
        links = []
        page = 'https://en.wikipedia.org' + page
        try:
            content = urllib.request.urlopen(page)
        except:
            print("failed to load: " + page)
            return None

        soup = BeautifulSoup(content, "html.parser")
        base=soup.find('div', id="bodyContent")

        for link in BeautifulSoup(str(base), "html.parser").findAll("a"):
            if 'href' in link.attrs:
                if 'pedia' not in link['href'] and 'http' not in link['href'] and 'Category' not in link['href'] and '#' not in link['href'] and 'disambiguation' not in link['href'] and 'File' not in link['href']:
                    links.append(link['href'])
        return links



    def loop(self):
        print('Finding the shortest path between the {} and {} pages...'.format(StartPage, TargetPage))

        while len(self.queue) and self.attempts < max_attempts:
                currentPage = self.queue.pop(0)

                currentPageLinks = self.GetLinksFromPage(currentPage)

                #check if page is empty
                if currentPageLinks == None:
                    continue

                #check if we have found Target
                if self.TargetPage in currentPageLinks:
                    print(self.paths[currentPage]+[self.TargetPage])
                    self.attempts += 1

                else:
                    for link in currentPageLinks:
                        if link not in self.paths[currentPage]:
                            self.queue.append(link)
                            self.paths[link] = self.paths[currentPage]+[link]





game = WTF(str(StartPage),str(TargetPage), max_attempts)
game.loop()