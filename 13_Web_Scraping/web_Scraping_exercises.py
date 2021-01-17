import requests
import bs4
import lxml


base_url = 'http://quotes.toscrape.com/page/{}'

res = requests.get(base_url.format('1'))

soup = bs4.BeautifulSoup(res.text, "lxml")

#print(soup)
#print(soup.select(".author"))
authors = set()
for name in soup.select(".author"):
    authors.add(name.text)

print(authors)

quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)

print(quotes)

soup.select(".tag-item")
for item in soup.select(".tag-item"):
    print(item.text)

url = 'http://quotes.toscrape.com/page/'
authors = set()
for page in range(1, 10):
    # concatenate to get a new page URL
    page_url = url+str(page)
    #obtain request
    res = requests.get(page_url)
    # turn into soup
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    # add authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)

print(authors)
list_authors = list(authors)
for name in list_authors:
    print(name)

# choose some huge page number we know doesn't exist
page_url = url+str(99999999)

# Obtain Request
res = requests.get(page_url)

# turn into soup
soup = bs4.BeautifulSoup(res.text, "lxml")

# print(soup)

# print("No quotes found!" in res.text)

page_still_valid = True
authors = set()
page = 1

while page_still_valid:

    # Concatenate to get new page URL
    page_url = url+str(page)

    # Obtain a request
    res = requests.get(page_url)

    # Check to ee if we're on the last page
    if "No quotes found!" in res.text:
        break

    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Add authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)

    page += 1

list_authors = []
list_authors = list(authors)
for name in list_authors:
    print(name)