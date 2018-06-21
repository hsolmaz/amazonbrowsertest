# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string
import time

char_set2 = string.ascii_lowercase + string.digits
random_number = char_set2.split('0')[1]
char_set = char_set2.split('0')[0]
random_numbers = ''.join(random.sample(random_number*1, 1))
i = int(random_numbers)
username = ''.join(random.sample(char_set*6, 6))
lastname = ''.join(random.sample(char_set*6, 6))
password = ''.join(random.sample(char_set*8, 8))
maildomain = ''.join(random.sample(char_set*6, 6))
usermail = username+'@'+maildomain+'.com'
category = [u'yamaç paraşütü', 'balon turu', u'dalıl', 'kitesurf',
            'yelkencilik', 'windsurf', 'paintball', 'atv safari', u'okçuluk', 'jeep safari']
driver = webdriver.Chrome()
driver.get("https://alt.test/")
""" driver.find_element_by_xpath('//*[@id="main-nav"]/li[5]/a').click()
driver.find_element_by_name(
    'fos_user_registration_form[name]').send_keys(username)
driver.find_element_by_name(
    'fos_user_registration_form[surname]').send_keys(lastname)
driver.find_element_by_name(
    'fos_user_registration_form[email]').send_keys(usermail)
driver.find_element_by_name(
    'fos_user_registration_form[plainPassword][first]').send_keys(password)
driver.find_element_by_name(
    'fos_user_registration_form[plainPassword][second]').send_keys(password)
driver.find_element_by_xpath(
    '//*[@id="user-actions"]/div/div/form/div/div[1]/div[9]/button').click() """
try:
    driver.find_element_by_xpath(
        '//*[@id="index-top-search"]/div/div[2]/div/input[1]').send_keys(category[i]+Keys.ENTER)
    driver.find_element_by_xpath(
        '//*[@id="index-top-search"]/div/div[4]/button').click()
    try:
        driver.execute_script(
            "document.getElementsByClassName('select2 select2-container select2-container--default select2-container--focus')[0].click()")
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="select-order"]/div[2]/ul/li[3]').click()
        time.sleep(5)
        str = driver.find_element_by_xpath(
            '//*[@id="search-page"]/div[3]/div[3]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div').text
        sayilar = [int(s) for s in str.split() if s.isdigit()]
        str = driver.find_element_by_xpath(
            '//*[@id="search-page"]/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[3]/div[2]/div').text
        sayilars = [int(s) for s in str.split() if s.isdigit()]
        if sayilar < sayilars:
            print u'Sıralama büyükten küçüğe çalışmaktadır'
    except Exception as e:
        print(e)
        print u'tek ürün mevcut'

        try:
            driver.find_element_by_xpath(
                '//*[@id="search-page"]/div[3]/div[3]/div[2]/div['+i+']/div/div[2]/div[1]/a').click()
        except:
            print u'tek ürün mevcut ilk ürün açıldı'
            driver.find_element_by_xpath(
                '//*[@id="search-page"]/div[3]/div[3]/div[2]/div[1]/div/div[2]/div[1]/a').click()

    time.sleep(10)
    driver.close()
except Exception as e:
    driver.close()
