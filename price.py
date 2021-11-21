import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys


url = "https://www.ozon.ru/category/elektronika-15500/?sorting=rating"

def webdriver_test():
    driver = webdriver_options('http://85.26.146.169', r"D:\\projects\\chromedriver\\chromedriver.exe", 0)
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(10)

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

def open_sellers(driver, vse):

    driver.find_element(By.XPATH, vse).click()


def select_seller(driver, seller):

    driver.find_element(By.XPATH, seller).click()
    time.sleep(2)


def get_tov(driver, tov):

    href = driver.find_element(By.XPATH, tov).get_attribute("href")
    return href

                    

def allq(url, zz, ww, s, p, vse, tov):

    hreffs = []
    for i in range(1, zz):
        try:
            driver = webdriver_options('http://85.26.146.169', r"D:\\projects\\chromedriver\\chromedriver.exe", 0)

            driver.get(url=url)
            time.sleep(2)
            open_sellers(driver, vse)
            time.sleep(2)
            select_seller(driver, f'//*[@id="layoutPage"]/div[1]/div[4]/div[{p}]/div[1]/aside/div[{s}]/div[2]/div[2]/div/span[{i}]/label/div[2]/span')
                                    
            hreffs.append(get_tov(driver, tov))

            with open(ww, 'w') as f:
                json.dump(hreffs, f)                        

            print("YYYYYYEEEEEEAAAAHHHH")
            print("YYYYYYEEEEEEAAAAHHHH")
            print(i, i, i, i, i)
            print("YYYYYYEEEEEEAAAAHHHH")
            print(i, i, i, i, i)
            print("YYYYYYEEEEEEAAAAHHHH")
            print(i, i, i, i, i)
            print("YYYYYYEEEEEEAAAAHHHH")
            print(i, i, i, i, i)

            time.sleep(2)

        
        except Exception as ex:
            print(ex)

        finally:
            driver.close()
    driver.quit()

def scroll(driver):
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    time.sleep(4)

def get_sel(driver):
    sel = driver.find_elements(By.CLASS_NAME, 'g4e6')
    sells = []
    for i in sel:
        sells.append(i.get_attribute("href"))

    return sells

def all_sells(urrl, namme):

    driver = webdriver_options('http://85.26.146.169', r"D:\\projects\\chromedriver\\chromedriver.exe", 1)
    driver.get(url=urrl)
    z = driver.find_element(By.XPATH, '//*[@id="layoutPage"]/div[1]/div[5]/div/div[2]/div[1]/span[1]').text
    zz = int(z.split(" ")[0])
    zz = zz // 11

    time.sleep(2)
    for i in range(zz):
        try:
            scroll(driver)
            sell = get_sel(driver)
            print(sell)

            try:
                with open(namme, encoding='utf-8') as file:
                    surv = json.load(file)
            except:
                qwqw = 1

            with open(namme, 'w') as f:
                json.dump(sell, f) 
            if sell == surv:
                break
                
                
            
        except Exception as ex:
            print(ex)




def send_addres(driver, adres, xpath_textarea, xpath_clean, xpath_select):

    otkuda = driver.find_element(By.XPATH, xpath_textarea)
    otkuda.send_keys(adres)
    if xpath_clean != 0:
        driver.find_element(By.XPATH, xpath_clean).click()
        otkuda.send_keys(adres)
    time.sleep(2)
    if xpath_select != 0:
        driver.find_element(By.XPATH, xpath_select).click()

def button_fix(driver):
    button = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div/div[2]/button')
    if button is not None:
        button.click()


def main(): 

    all_sells('https://www.ozon.ru/seller?category=14500', "dom-i-sad-14500.json")
    all_sells('https://www.ozon.ru/seller?category=17777', "obuv-17777.json")
    all_sells('https://www.ozon.ru/seller?category=7500', "odezhda-obuv-i-aksessuary-7500.json")
    all_sells('https://www.ozon.ru/seller?category=15500', "elektronika-15500.json")


    

main()

