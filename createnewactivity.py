# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string
import time

for x in range(25):
    char_set2 = string.ascii_lowercase + string.digits
    random_number = char_set2.split('0')[1]
    lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque lobortis, turpis auctor vehicula feugiat, metus metus commodo mauris, ac bibendum nulla augue sit amet ante. Praesent malesuada ipsum risus, eget faucibus nulla aliquet non. Nullam cursus viverra nisi, sit amet tempor felis viverra ut. Sed semper libero ipsum, sed hendrerit leo dapibus nec. Ut consequat arcu lorem, congue congue diam varius vel. Mauris gravida sed diam sit amet ultricies. Ut id pharetra sapien'
    char_set = char_set2.split('0')[0]
    random_numbers = ''.join(random.sample(random_number*1, 1))
    i = int(random_numbers)
    random_numbers = ''.join(random.sample(random_number*3, 3))
    kon = int(random_numbers)
    random_numbersi = ''.join(random.sample(random_number*1, 1))
    ix = int(random_numbersi)
    random_numbersi = ''.join(random.sample(random_number*1, 1))
    dive = int(random_numbersi)
    divs = ['1', '2', '3', '3',
            '1', '2', '3', '1', '1', '2', '3', '2']

    category = ['yamac parasutu', 'balon turu', 'dalil', 'kitesurf',
                'yelkencilik', 'windsurf', 'paintball', 'atv safari', 'okculuk', 'jeep safari']

    word = ['activity', 'Holiday', 'product', 'blue',
            'green', 'Yellow', 'Red', 'brown', 'ping', 'purple', ]
    words = ["geeks", "for", "geeks", "a",
             "portal", "to", "learn", "can", "be",
             "computer", "science", "zoom", "yup",
             "fire", "in", "be", "data", "geeks"]
    activityname = 'selam'
    activityname = word[i]+' '+words[i]+' ' + \
        word[ix]+' '+words[ix]+' '+category[i]+' '
    print activityname+' '+' '+divs[dive]
    print kon
    driver = webdriver.Chrome()
    driver.get("https://alt.test/admin/product/wizard")
    driver.find_element_by_xpath(
        '//*[@id="steps-uid-0-p-0"]/div/div[2]/div/div/div/div[1]/a').click()
    driver.find_element_by_xpath(
        '//*[@id="steps-uid-0"]/div[3]/ul/li[2]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="steps-uid-0-p-1"]/div/div[2]/div/div/div/div[' +
        divs[dive]+']/div/div[2]/ul/li['+divs[dive]+']').click()

    driver.find_element_by_xpath(
        '//*[@id="steps-uid-0"]/div[3]/ul/li[3]/a').click()

    driver.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div/div[2]/div/div/div/label/span[1]').click()
    driver.find_element_by_id(
        'select2-city-container').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/span/span/span[1]/input').send_keys('izmir'+Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_id('select2-district-container').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/span/span/span[1]/input').send_keys('fo'+Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="language-tr"]/div[3]/input').send_keys(Keys.TAB+activityname+Keys.TAB+lorem+Keys.TAB+words[i]+Keys.TAB+word[ix]+Keys.TAB+words[i])
    driver.find_element_by_xpath(
        '//*[@id="language-tr"]/div[1]/input').send_keys(activityname)
    driver.find_element_by_id('dateprice').click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="month-tab-2018-06"]/div[2]/div/div[2]/input').send_keys(dive)
    driver.find_element_by_xpath(
        '//*[@id="month-tab-2018-06"]/div[2]/div/div[1]/a').click()
    driver.find_element_by_xpath(
        '//*[@id="month-tab-2018-06"]/div[2]/div/div[3]/input').send_keys(kon)
    driver.find_element_by_xpath(
        '//*[@id="month-tab-2018-06"]/div[2]/div/div[4]/button').click()
    driver.execute_script("window.scrollTo(500, 0)")
    driver.find_element_by_xpath(
        '/html/body/div[2]/div/div/div/div/div[2]/div/div/button').click()
    driver.close()
