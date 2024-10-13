import requests
from article import article
from bs4 import BeautifulSoup

def scroll_through():
    """scrolls through a sectionn of the website and scrapes the articles until it cannot anymore"""

def scrape_article(url, genre):
    """scrapes the article from the website, and returns an article object"""
    # takes a url and stores the html in a variable
    webpage = requests.get(url)
    webpagetext = webpage.text
    # uses beautiful soup to parse the html
    soup = BeautifulSoup(webpagetext, 'html.parser')
    # finds the title, author, genre, and content of the article
    title = soup.find('h1', 'post-title').text
    byline = soup.find('div', 'post-byline').text
    author = byline.split("on")[0][3:]
    date = byline.split("on")[1]
    content=soup.find('div', 'post-content').text

    # creates an article object and returns it
    return article(title, author, date, genre, content)

def main(): 
    print("Hello World")
    sample_article = scrape_article("http://eic.opalstacked.com/masters-at-work-mills-mfa-artists-discuss-the-show-and-their-inspiration/", "Arts & Entertainment")
    sample_article.display()

if __name__=="__main__":
    main()