from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, WebDriverException

import time, requests, os




def insta(user,passwd):
    browser = webdriver.Firefox()
    
    try:
        browser.get("https://www.instagram.com/direct/inbox/")
        time.sleep(2)

        username = browser.find_element_by_name("username")
        password = browser.find_element_by_name("password")

        username.send_keys(user)
        password.send_keys(passwd)
        loginButton = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/form/div/div[3]/button")
        loginButton.click()
    except ElementClickInterceptedException as error:
        #browser.close()
        return str("kullanıcı girişinde sorun oldu")

    try:
        time.sleep(5)
        NTbutton = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        NTbutton.click()
        time.sleep(5)

        get_messages = browser.find_elements_by_xpath('//a[@class ="-qQT3 rOtsg"]')
        sayac = len(get_messages)
        for k in range(1,sayac+1):
            class_name = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[1]/a')
            class_name.click()
            time.sleep(1)
            infButton = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/button')
            infButton.click()
            time.sleep(1)

            removeButton = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div[1]/button')
            removeButton.click()
            time.sleep(1)

            actionButton = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/button')
            actionButton.click()
            browser.refresh()
            time.sleep(5)

    except ElementClickInterceptedException as error:
        #browser.close()
        return str("Mesaj alanı algılanamadı...")

    #browser.close()
    #return str("Mesajlar Silindi...")

def scroll(driver, count):
    

    # Get scroll height
    #last_height = driver.execute_script("return document.body.scrollHeight")
    scrollCount = count
    NewScrollCount = 0
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        NewScrollCount += 1
        time.sleep(2)
        if NewScrollCount == scrollCount:
            break


