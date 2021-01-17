import requests
import lxml
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup = bs4.BeautifulSoup(res.text, 'lxml')

image_info = soup.select('.thumbimage')

print(image_info)

print(len(image_info))

computer = image_info[0]

print(type(computer))

print(computer['src'])

image_link = requests.get('http://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')

print(type(image_link))
print(image_link.content)

f = open('my_new_file_name.jpg', 'wb')

f.write(image_link.content)

f.close()

