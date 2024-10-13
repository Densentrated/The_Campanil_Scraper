import requests
from article import article
from bs4 import BeautifulSoup

def scroll_through(url):
    """scrolls through a sectionn of the website and scrapes the articles until it cannot anymore, returns an array of links"""
    # uses find() to get all of the links for an article
    # sees if there is a next page
    # do while loop

    isNext = True
    links = []
    counter = 1

    while True: 
        # gets the text of the webpage
        webpage = requests.get(url)
        webpagetext = webpage.text
        soup = BeautifulSoup(webpagetext, 'html.parser')

        # finds all of the article links and appends them to the list
        for chunk in soup.find_all('h2', 'post-title'):
            link = chunk.find('a')['href']
            links.append(link)
                
        # end if there is no next page  
        isNext = soup.find('a', 'next page-numbers') is not None

        if not isNext:
            break

        # updates the terminal
        print(f"scraped page {counter}")
        counter += 1

        # updates the url to the next page
        url = soup.find('a', 'next page-numbers')['href']

    return links


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
    content = soup.find('div', 'post-content').text.replace('\n', '')

    # creates an article object and returns it
    return article(title, author, date, genre, content)

def get_articles(links, genre):
    """takes an array of links and a genre and returns an array of article objects"""
    print("getting articles for " + genre)
    articles = []
    counter = 1
    for link in links:
        articles.append(scrape_article(link, genre))
        print(f"scraped article {counter} out of {len(links)}")
        counter += 1
    return articles

def main(): 

    # gets links for every categroy of article
    news = scroll_through('http://eic.opalstacked.com/category/news/')
    arts_and_entertainment = scroll_through('http://eic.opalstacked.com/category/ae/')
    opinions = scroll_through('http://eic.opalstacked.com/category/opinions/')
    health = scroll_through('http://eic.opalstacked.com/category/health/')
    science_and_tech = scroll_through('http://eic.opalstacked.com/category/science-technology/')

    articles = []
    articles.extend( get_articles(news, "news"))
    articles.extend(get_articles(arts_and_entertainment, "arts and entertainment"))
    articles.extend( get_articles(opinions, "opinions"))
    articles.extend( get_articles(health, "health"))
    articles.extend( get_articles(science_and_tech, "science and technology"))

    # puts articles in a csv file
    #with open('article.csv', 'w') as f:
    #    f.write("title,author,genre,date,content\n")

    with open('articles.csv', 'a') as f:
        for article in articles:
            f.write(article.to_csv() + '\n')


if __name__=="__main__":
    main()