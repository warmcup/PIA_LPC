import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
job_elements = soup.find_all('div', class_='card-content')

for job_element in job_elements:
    print(job_element, end='\n'*2)
