import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
job_elements = soup.find_all('div', class_='card-content')
python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())

print(len(python_jobs))