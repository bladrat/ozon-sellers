import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
import pickle



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



def open_lamp(driver):
    driver.find_element(By.CLASS_NAME, "ui-b4.ui-c5.ui-e3").click()
    time.sleep(1)

def get_buz(driver):
    buzy = []
    stroks = driver.find_elements(By.CLASS_NAME, "e7j9")
    for i in stroks:
        buzy.append(i.text)
    return buzy

def name_buz(driver):
    return driver.find_element(By.CLASS_NAME, "e7j6").get_attribute('title')

def get_dostav(driver):
    dostavka = driver.find_element(By.CLASS_NAME, 'b7j5')

    try:
        if dostavka.find_element(By.CLASS_NAME, 'e6n6').text == "Ozon":
            sklad = "Склад Ozon"
    except:
        q = 1
    try:
        if dostavka.find_element(By.CLASS_NAME, 'e6n5').text == "Доставка со склада продавца":
            sklad = "Склад продавца"
    except:
        q = 1
    

    metods = driver.find_elements(By.CLASS_NAME, "c3q5")
    m1 = metods[0].find_element(By.TAG_NAME, 'span').find_element(By.TAG_NAME, 'span').text
    print("qfijowrogowirgowrogihhio")
    print(metods[1].find_element(By.TAG_NAME, 'span').find_element(By.TAG_NAME, 'span').text)
    print(sklad)

def get_seller_info(url):
    try:
        tovars = []
        driver = webdriver_options('http://85.26.146.169', r"D:\\projects\\chromedriver\\chromedriver.exe", 0)
        driver.get(url)
        time.sleep(2)
        open_lamp(driver)
        time.sleep(1)
        get_buz(driver)
        name_buz(driver)
        get_dostav(driver)
        
    finally:
        driver.close() 



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
        cookie_update(driver)
        time.sleep(2)
        open_sellers(driver)
        for elem in range(len_seller(driver)):
            try:
                driver.get(url)
                cookie_update(driver)
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




def get_cookie(url):
    driver = webdriver_options('http://85.26.146.169', r"D:\\projects\\chromedriver\\chromedriver.exe", 0)
    driver.get(url)

    time.sleep(20)
    pickle.dump(driver.get_cookies(), open(f"cookies", "wb"))

def cookie_update(driver):
    for cookie in pickle.load(open(f"cookies", "rb")):
        driver.add_cookie(cookie)
    driver.refresh()

main("https://www.ozon.ru/category/tovary-dlya-vzroslyh-9000/", "tovary-dlya-vzroslyh-9000.json")
main("https://www.ozon.ru/category/elektronnye-sigarety-i-tovary-dlya-kureniya-35659/", "elektronnye-sigarety-i-tovary-dlya-kureniya-35659.json")