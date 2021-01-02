from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import time


def login():
    driver = webdriver.Chrome(executable_path='C:\chrome_driver_win32\chromedriver.exe')

    driver.get('https://www.linkedin.com/')
    driver.maximize_window()
    email= driver.find_element_by_xpath('//*[@id="login-email"]')
    email.send_keys('dimple97verma@gmail.com')                   #enter ur email-id
    time.sleep(3)

    password=driver.find_element_by_xpath('//*[@id="login-password"]')
    password.send_keys('******')                                  #enter password
    time.sleep(3)

    sign_in=driver.find_element_by_xpath('//*[@id="login-submit"]')
    sign_in.click()
    time.sleep(3)
    search=driver.find_element_by_xpath('//*[starts-with(@id, "ember")]/input')
    search.clear()
    search.send_keys('python developer'+'\n')
    wait = WebDriverWait(driver, 120)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Jobs"]')))
    element.click()
    time.sleep(10)
    location=driver.find_element_by_xpath('//input[@placeholder="Search location"]')
    location.clear()
    location.send_keys('Pune,Maharashtra,India')
    time.sleep(1)
    search_button=driver.find_element_by_xpath('//button[text()="Search"]')
    search_button.click()

    # ele1=driver.find_elements_by_xpath('//*[starts-with(@id, "ember"]/form/button/div/div/h3')
    # ele2=driver.find_element_by_xpath('//*[@id="experience-level-facet-values"]/li[1]/label/p/span[1]')
    # hover=ActionChains(driver).move_to_element(ele1).click(ele2).perform()
    # experience=driver.find_element_by_xpath('//*[@id="experience-level-facet-values"]/li[1]/label/p/span[1]')
    # experience.click()


    soup = BeautifulSoup(driver.page_source, 'lxml')
    items=soup.find('ul',class_='card-list card-list--column jobs-search-results__list')

    for a in items.find_all('a'):
       print  "https://www.linkedin.com"+a['href']

login()
