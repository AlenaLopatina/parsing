from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

def parser_hh(vacancy):
    vacancy_date = []

    params = {
        'text': vacancy,
        'search_field': 'name',
        'items_on_page': '20',
        'page': ''
    }


    link = 'https://hh.ru/search/vacancy'

    html = requests.get(link, params=params)

    if html.ok:
        parsed_html = bs(html.text, 'html.parser')

        page_block = parsed_html.find('div', {'data-qa': 'pager-block'})
        if not page_block:
            last_page = '1'
        else:
            last_page = int(page_block.find_all('a', {'class': 'HH-Pager-Control'})[-2].getText())

    for page in range(0, last_page):
        params['page'] = page
        html = requests.get(link, params=params, headers=headers)

        if html.ok:
            parsed_html = bs(html.text, 'html.parser')

            vacancy_items = parsed_html.find('div', {'data-qa': 'vacancy-serp__results'}) \
                .find_all('div', {'class': 'vacancy-serp-item'})

            for item in vacancy_items:
                vacancy_date.append(parser_item_hh(item))

    return vacancy_date

def parser_item_hh(item):
    vacancy_date = {}

    vacancy_name = item.find('div', {'class': 'resume-search-item__name'}) \
        .getText() \
        .replace(u'\xa0', u' ')

    vacancy_date['vacancy_name'] = vacancy_name

    salary = item.find('div', {'class': 'vacancy-serp-item__compensation'})
    if not salary:
        salary_min = None
        salary_max = None
        salary_currency = None
    else:
        salary = salary.getText() \
            .replace(u'\xa0', u'')

        salary = re.split(r'\s|-', salary)

        if salary[0] == 'до':
            salary_min = None
            salary_max = int(salary[1])
        elif salary[0] == 'от':
            salary_min = int(salary[1])
            salary_max = None
        else:
            salary_min = int(salary[0])
            salary_max = int(salary[1])

        salary_currency = salary[2]

    vacancy_date['salary_min'] = salary_min
    vacancy_date['salary_max'] = salary_max
    vacancy_date['salary_currency'] = salary_currency

    vacancy_link = item.find('div', {'class': 'resume-search-item__name'}) \
        .find('a')['href']


    vacancy_date['vacancy_link'] = vacancy_link

    vacancy_date['site'] = 'hh.ru'

    return vacancy_date


def parser_vacancy(vacancy):
    vacancy_date = []
    vacancy_date.extend(parser_hh(vacancy))
    df = pd.DataFrame(vacancy_date)
    return df

vacancy = 'Python'
df = parser_vacancy(vacancy)