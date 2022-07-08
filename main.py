from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drv = webdriver.Chrome('chromedriver.exe')
drv.get('http://google.com/ncr')
assert 'Google' in drv.title
elem = drv.find_element(by='name', value='q')
elem.send_keys('selenide')
elem.send_keys(Keys.RETURN)
txt = drv.find_element(by='xpath', value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/div/cite').text[-12:]
assert 'selenide.org' == txt
drv.find_element(by='xpath', value='//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
txt = drv.find_element(by='xpath', value='//*[@id="islrg"]/div[1]/div[1]/a[2]/div').text
assert 'selenide.org' != txt
drv.find_element(by='xpath', value='//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]').click()
txt = drv.find_element(by='xpath', value='//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite').text[-12:]
assert 'selenide.org' == txt
drv.close()
