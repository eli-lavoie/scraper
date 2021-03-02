import requests
from bs4 import BeautifulSoup as bs


URL = "https://www.monster.com/jobs/search/?q=software-engineer&where=nashville-tn&intcid=skr_navigation_nhpso_searchMain"
page = requests.get(URL)


page_content = bs(page.content, 'html.parser')

job_cards = page_content.find_all('section', class_="card-content")

for card in job_cards:
  job_title = card.find('h2', class_='title')
  company = card.find('div', class_='company')
  location = card.find('div', class_='location')

  if None in (job_title, company, location):
    continue

  print('Title: ', job_title.text.strip())
  print('Company: ', company.text.strip())
  print('Location: ', location.text.strip())

