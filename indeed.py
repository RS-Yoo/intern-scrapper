import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://www.indeed.com/jobs?q=software%20engineer%20intern&limit={LIMIT}"


def extract_indeed_pages():
    start = 0
    start_int_list = [0]
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, 'html.parser')

    next_button = soup.find("a", {"aria-label": "Next"})

    while next_button:
        URL_updated = f"https://kr.indeed.com/jobs?q=python&limit=50&start={str(start)}"
        result_updated = requests.get(URL_updated)
        soup_updated = BeautifulSoup(result_updated.text, 'html.parser')
        next_button = soup_updated.find("a", {"aria-label": "Next"})
        if next_button is None:
            break

    start = int(start) + 50
    start_int_list.append(start)

    return start_int_list[-1]


def extract_indeed_jobs(last_page):
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page * LIMIT}")
        print(result.status_code)
