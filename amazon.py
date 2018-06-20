from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.amazon.com")
driver.find_element_by_id('nav-link-accountList').click()
driver.find_element_by_id('ap_email').send_keys('angealhelwey@gmail.com')
driver.find_element_by_id('continue').click()
driver.find_element_by_id('ap_password').send_keys('12801988')
driver.find_element_by_id('a-autoid-0').click()
driver.find_element_by_id(
    'twotabsearchtextbox').send_keys('samsung'+Keys.RETURN)
searchName = driver.find_element_by_id('s-result-count').text
if searchName == '1-16 of over 30,000 results for "samsung"':
    print 'Searched for samsung'
else:
    print 'Error: Results not for samsung'
driver.find_element_by_xpath('//*[@id="pagn"]/span[3]').click()
pageNumber = driver.find_element_by_id('s-result-count').text
if '17-32 of over 30,000 results for "samsung"' == pageNumber:
    print 'You are in second page'
else:
    print 'Error : You are in second page'
driver.find_element_by_xpath(
    '//*[@id="result_18"]/div/div/div/div[2]/div[1]/div[1]/a/h2').click()
productName = driver.find_element_by_id('productTitle').text
driver.find_element_by_xpath('//*[@id="add-to-wishlist-button"]').click()
driver.implicitly_wait(1)
try:
    driver.find_element_by_id('atwl-list-name-MVFI5K0B7J10').click()
except:
    driver.find_element_by_id('atwl-list-name-MVFI5K0B7J10').click()

driver.implicitly_wait(3)
favoriteName = driver.find_element_by_xpath(
    '//*[@id="WLHUC_info"]/div[1]/ul/li[2]/table/tbody/tr[1]/td/a').text
driver.find_element_by_xpath('//*[@id="WLHUC_viewlist"]').click()
if favoriteName == productName:
    print 'Product name is correct'
else:
    print productName
    print favoriteName
    print 'First one is you want to add your wish list \n second one is your added favorite item name'
driver.find_element_by_name('submit.deleteItem').click()
driver.implicitly_wait(2)
if driver.find_element_by_xpath('//*[@id="g-items"]').text.split('\n')[-2] == 'Delete':
    print 'Product deleted on favorite'
else:
    print 'Error : You didn\'t deleted'
driver.implicitly_wait(2)
driver.close()
