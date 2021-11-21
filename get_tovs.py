import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys





def webdriver_options(proxy, path, headless):
    
    #Настраиваем вебдрайвер прописываем прокси, путь к драйверу и режим хеадлесс
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent={useragent.random}")
    options.add_argument(proxy)
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    #тихий режим работы
    if headless == 1:
        options.add_argument('headless')

    return  webdriver.Chrome(executable_path=path, options=options)

def open_sellers(driver):
    driver.find_elements(By.CLASS_NAME, "show")[-1].click()
    time.sleep(1)

def len_seller(driver):
    sellers_filt = driver.find_element(By.CLASS_NAME, "g1n3")
    sellers = sellers_filt.find_elements(By.CLASS_NAME, "g1p7")
    return(len(sellers))

def select_seller(driver, elem):

    sellers_filt = driver.find_element(By.CLASS_NAME, "g1n3")
    sellers = sellers_filt.find_elements(By.CLASS_NAME, "g1p7")
    sellers[elem].click()

def get_tovar(driver):

    tovar = driver.find_element(By.CLASS_NAME, "b0c8.tile-hover-target").get_attribute("href")
    return tovar


def main(url, name):
    try:
        tovars = []
        driver = webdriver_options('http://85.26.146.169', r"D:\\projects\\chromedriver\\chromedriver.exe", 1)
        driver.get(url)
        open_sellers(driver)
        for elem in range(len_seller(driver)):
            try:
                driver.get(url)
                time.sleep(2)
                try:
                    open_sellers(driver)
                except:
                    fadfdf = 1
                time.sleep(2)
                select_seller(driver, elem)
                time.sleep(3)
                tovars.append(get_tovar(driver))

                with open(name, 'w') as f:
                    json.dump(tovars, f)
                print("YYYYYYEEEEEEAAAAHHHH")
                print("YYYYYYEEEEEEAAAAHHHH")
                print(elem, elem, elem, elem, elem)
                print("YYYYYYEEEEEEAAAAHHHH")
                print(elem, elem, elem, elem, elem)
                print("YYYYYYEEEEEEAAAAHHHH")
                print(elem, elem, elem, elem, elem)
                print("YYYYYYEEEEEEAAAAHHHH")
                print(elem, elem, elem, elem, elem)

            except Exception as ex:
                print(ex)
                print("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo")
                print("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo")
                print("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo")
                print("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo")

    finally:
        driver.close() 


main("https://www.ozon.ru/category/elektronika-15500/?sorting=rating", "elektronika-15500.json")
