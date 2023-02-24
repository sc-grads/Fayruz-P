import requests
from bs4 import BeautifulSoup
import openpyxl

url = 'https://www.imdb.com/search/title/?release_date=2019-01-01,2309-12-31&sort=num_votes,desc'
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')
content = soup.find_all('div', class_='lister-item-content')
movies = list()

for item in content:
    name = item.h3.a.text
    rating = item.strong.text
    movies.append((name,rating))

print(movies)

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'IMBD Movies'
sheet['A1']= 'Year'
sheet['B1']= 'Movie'

for movie in movies:
    sheet.append(movie)

wb.save('movies-2019.xlxs')