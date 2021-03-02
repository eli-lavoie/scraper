import requests


URL = "https://www.monster.com/jobs/search/?q=software-engineer&where=nashville-tn&intcid=skr_navigation_nhpso_searchMain"
page = requests.get(URL)

print(page.content)