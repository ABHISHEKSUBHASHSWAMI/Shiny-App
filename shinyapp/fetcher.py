
import bs4
import requests
import re

global headers
#define browswer headers
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}

#function for fetching url
def url_fetcher(url):

    #create a request object
    req = requests.get(url, headers)

    #creating a soup object
    soup = bs4.BeautifulSoup(req.content, 'html.parser')

    #list to store urls
    urls=[]

    #exception urls
    ex="https://en.wikipedia.org/wiki/Special:Search"

    for link in soup.find_all('a',attrs={'href': re.compile("https://en.wikipedia")}):
        urls.append(link.get('href'))

    if urls[-1]==ex:
        return 0
        
    else:
        return urls[-1]

#function for text fetcher
def text_fetcher(url):

    if (url !=""):
        source=requests.get(url,headers)

        #create soup object
        textsoup = bs4.BeautifulSoup(source.content, "html.parser")

        # Extract the plain text content from paragraphs
        paras = []
        for paragraph in textsoup.find_all('p'):
            paras.append(str(paragraph.text))
    
        text = ' '.join(paras)

        # Drop footnote superscripts in brackets
        text = re.sub(r"\[.*?\]+", '', text)

        # Replace '\n' (a new line) with '' and end the string at $1000.
        text = text.replace('\n', '')
        return text

    else:
        return "Waiting for url..."

def wiki_fetcher(url):

    data=url_fetcher(url)
    if data==0:
        warning="Nothing Found !"
        return warning
    else:
        text=text_fetcher(data)
        index=text.find("version.")
        return (text[index+9:])

#query to url conversion
def query_to_url(query):

    query=list(map(str,query.strip().split(" ")))
    q_url='https://en.wikipedia.org/w/index.php?go=Go&search='+'+'.join(query)
    return q_url
