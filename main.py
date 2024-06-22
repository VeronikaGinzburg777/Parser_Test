import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the webdriver
driver = webdriver.Chrome()

try:
    url = "https://www.divan.ru/category/nastolnye-lampy"
    driver.get(url)

    time.sleep(3)

    lamps = driver.find_elements(By.CLASS_NAME, 'WdR1o')
    print(f"Найдено настольных ламп: {len(lamps)}")
    parsed_data = []

    for lamp in lamps:
        try:
            name = lamp.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
            price = lamp.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
            url = lamp.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            print(name, price, url)
            parsed_data.append([name, price, url])
        except Exception as e:
            print(f"Произошла ошибка при парсинге лампы: {e}")
            continue

finally:
    driver.quit()

with open("divan_lamps.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название лампы', 'Цена', 'URL'])
    writer.writerows(parsed_data)
