import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the URL
url = "https://tomsk.hh.ru/vacancies/programmist"
driver.get(url)

# Allow time for the page to load
time.sleep(3)

#<span class="vacancy-name--c-19Lay3KouCl7XasYakLk serp-item__title-link" data-qa="serp-item__title">Инженер-программист</span>
# Find the vacancies


vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--z_UXteNo7bRGzxWVcL7y')
print(vacancies)
parsed_data = []

# Iterate through the vacancies
for vacancy in vacancies:
    try:
        # Extract details of each vacancy

        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--c1Lay3KouCl7XasYakLk').text
        print(salary)
        parsed_data.append([salary])
    except Exception as e:
        print(f"произошла ошибка при парсинге: {e}")
        continue

# Quit the driver after parsing all vacancies
driver.quit()

# Write the data to a CSV file
with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['зарплата'])
    writer.writerows(parsed_data)
