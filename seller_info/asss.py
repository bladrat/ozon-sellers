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

def open_lamp(driver):
    driver.find_element(By.CLASS_NAME, "ui-b4.ui-c5.ui-e3").click()
    time.sleep(1)

def get_buz(driver):
    buzy = []
    stroks = driver.find_elements(By.CLASS_NAME, "e7j9")
    for i in stroks:
        buzy.append(i.text)
    print(buzy)

def name_buz(driver):
    print(driver.find_element(By.CLASS_NAME, "e7j6").get_attribute('title'))

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
    print(metods[0].find_element(By.TAG_NAME, 'span').find_element(By.TAG_NAME, 'span').text)
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


main("https://www.ozon.ru/category/elektronika-15500/?sorting=rating", "elektronika-15500.json")
