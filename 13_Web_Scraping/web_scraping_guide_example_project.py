import requests
import lxml
import bs4

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format('1'))

soup = bs4.BeautifulSoup(res.text, "lxml")

print(soup.select(".product_pod"))

products = soup.select(".product_pod")

example = products[0]

print(type(example))

print(example.attrs)

print(list(example.children))

print(example.select('.star-rating.Three'))
print(example.select('.star-rating.Two'))

print(example.select('a'))

print(example.select('a')[1])


print(example.select('a')[1]['title'])


two_star_titles = []

for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, "lxml")
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_titles.append(book.select('a')[1]['title'])

print(two_star_titles)

for item in two_star_titles:
    print(item)
    