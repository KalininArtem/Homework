import json
import time
from copy import deepcopy

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=option)

driver.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2')

xpath_vacancies = ('//div[contains(@class,"serp-item") '
                   'and contains(@data-qa,"vacancy-serp__vacancy")]')

vacancies = WebDriverWait(driver, 1).until(
    EC.presence_of_all_elements_located((By.XPATH, xpath_vacancies))
)

count_vacancies = len(vacancies)
print(f'Найдено вакансий {count_vacancies}')

time.sleep(3)
list_links_vacancies = []
for vacancy in vacancies:
    try:
        salary_el = WebDriverWait(vacancy, 0.1).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 './/span[@data-qa="vacancy-serp__vacancy-compensation"]'))
        )
        salary_text = salary_el.text
    except Exception as e:
        print('Размер оплаты труда вакансии не найден')
    else:
        if '$' in salary_text:
            link_el = WebDriverWait(vacancy, 1).until(
                EC.element_to_be_clickable(
                    (By.XPATH, './/h3[@data-qa="bloko-header-3"]//a'))
            )
            link = link_el.get_attribute('href')
            list_links_vacancies.append(link)

count_dollar_vacancies = len(list_links_vacancies)
print(f'Найдено вакансий в долларах {count_dollar_vacancies}')

parsed_vacancies = []

for link in list_links_vacancies:

    driver.get(link)
    time.sleep(2)

    current_url = driver.current_url
    print(f'Работаем со ссылкой {current_url}')

    try:
        description_el = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="vacancy-description"]'))
        )

        description_text = description_el.text
    except Exception as e:
        print('Описание компании не найдено')
    else:
        if ('flask' in description_text.lower() or
                'django' in description_text.lower()):

            company_name = None
            title_vacancy = None
            salary_vacancy = None
            city = None

            try:
                salary_vacancy_el = WebDriverWait(driver, 0.1).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//div[@data-qa="vacancy-salary"]'))
                )
                salary_vacancy = salary_vacancy_el.text
            except Exception as e:
                print('Размер оплаты труда вакансии не найден')

            try:
                company_name_el = WebDriverWait(driver, 0.1).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//a[@data-qa="vacancy-company-name"]'))
                )
                company_name = company_name_el.text
            except Exception as e:
                print('Наименование компании не найдено')
            try:
                title_vacancy_el = WebDriverWait(driver, 0.1).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//h1[@data-qa="vacancy-title"]'))
                )
                title_vacancy = title_vacancy_el.text
            except Exception as e:
                print('Наименование вакансии не найдено')

            try:
                city_el = WebDriverWait(driver, 0.1).until(
                    EC.element_to_be_clickable(
                        (By.XPATH,
                         '//span[@data-qa="vacancy-view-raw-address"] | '
                         '//p[@data-qa="vacancy-view-location"]'))
                )
                city = city_el.text
            except Exception as e:
                print('Город вакансии не найден')

            parsed_vacancies.append(deepcopy(
                {
                    'Ссылка': current_url,
                    'Вилка зп': salary_vacancy or 'Не указано',
                    'Название компании': company_name or 'Не указано',
                    'Город': city or 'Не указан',
                })
            )

with open('output.json', 'w', encoding='utf-8') as file:
    json.dump(parsed_vacancies, file, indent=4, ensure_ascii=False)

print('Программа окончила работу')
