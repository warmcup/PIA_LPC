# Autor: Juan Angel Garza Castillo
# Matricula: 2007612

import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
job_elements = soup.find_all('div', class_='card-content')
python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())
python_jobs_elements = [element.parent.parent.parent for element in python_jobs]

for job_element in python_jobs_elements:
    title_element = job_element.find('h2', class_='title')
    company_element = job_element.find('h3', class_='company')
    location_element = job_element.find('p', class_='location')
    link_url = job_element.find_all('a')[1]['href']
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(f'Apply here: {link_url}\n')
    print()
