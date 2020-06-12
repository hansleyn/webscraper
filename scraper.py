# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium.webdriver import Chrome
import pandas as pd
import math

webdriver = "chromedriver"

driver = Chrome(webdriver)

urls = {}

urls['Africa'] = 'https://www.skyscrapercenter.com/x/11695362'
urls['Asia'] = 'https://www.skyscrapercenter.com/x/11695399'
urls['Central America'] = 'https://www.skyscrapercenter.com/x/11695400'
urls['Europe'] = 'https://www.skyscrapercenter.com/x/11695401'
urls['Middle East'] = 'https://www.skyscrapercenter.com/x/11695405'
urls['North America'] = 'https://www.skyscrapercenter.com/x/11695409'
urls['Oceania'] = 'https://www.skyscrapercenter.com/x/11695412'
urls['South America'] = 'https://www.skyscrapercenter.com/x/11695415'


region = 'South America'
url = urls[region]
    
driver.get(url)

path_results = '//*[@id="resultsBanner"]/div/strong[1]'

results = float((driver.find_element_by_xpath(path_results).text).replace(",", ""))
if results<700:
    last_page = math.ceil(results/50)
else:
    last_page = math.ceil(results/100)

total = []

for i in range(last_page):  #########################################

    items = len(driver.find_elements_by_class_name("building-hover"))
    
    
    for j in range(1, items + 1):
        
        path_num = '#table-baseList > tbody > tr:nth-child(' + str(j) + ') > td.sorting_1'
        num = int(driver.find_element_by_css_selector(str(path_num)).text)
        
        ################ STATUS PENDING
        #table-baseList > tbody > tr:nth-child(25) > td.status
        path_status = '//*[@id="table-baseList"]/tbody/tr[' + str(j) + ']/td[2]'
        status = driver.find_element_by_xpath(str(path_status)).text
        ################
        
        path_name = '//*[@id="table-baseList"]/tbody/tr[' + str(j)+ ']/td[3]/a'
        name = driver.find_element_by_xpath(str(path_name)).text
                
        path_city = '//*[@id="table-baseList"]/tbody/tr[' + str(j)+ ']/td[4]/a'
        city = driver.find_element_by_xpath(str(path_city)).text
        
        path_country = '//*[@id="table-baseList"]/tbody/tr[' + str(j)+ ']/td[4]/a[2]'
        country = driver.find_element_by_xpath(str(path_country)).text
        
        path_height_m = '//*[@id="table-baseList"]/tbody/tr[' + str(j)+ ']/td[5]'
        height_m = (driver.find_element_by_xpath(str(path_height_m)).text)
        
        path_height_ft = '//*[@id="table-baseList"]/tbody/tr[' + str(j)+ ']/td[6]'
        height_ft = ((driver.find_element_by_xpath(str(path_height_ft)).text).replace(",", ""))
        
        path_floors = '//*[@id="table-baseList"]/tbody/tr[' + str(j)+ ']/td[7]'
        floors = (driver.find_element_by_xpath(str(path_floors)).text).replace("-", "Unknown")
        
        path_completion = '//*[@id="table-baseList"]/tbody/tr[' + str(j)+ ']/td[8]'
        completion = (driver.find_element_by_xpath(str(path_completion)).text).replace("-", "Unknown")
        
        path_material = '//*[@id="table-baseList"]/tbody/tr[' + str(j)+ ']/td[9]'
        material = (driver.find_element_by_xpath(str(path_material)).text).replace("-", "Unknown")
        
        path_use = '//*[@id="table-baseList"]/tbody/tr[' + str(j)+ ']/td[10]'
        use = (driver.find_element_by_xpath(str(path_use)).text).replace("-", "Unknown")
        
        new = ((num, name, city, country, status, height_m, height_ft, floors, completion, material, use))
        total.append(new)
    print("page" + " " + str(i))    
    path_next_page = '//*[@id="table-baseList_next"]'
    next_button = driver.find_element_by_xpath(path_next_page)
    next_button.click()


df = pd.DataFrame(total, columns=['num', 'name', 'city', 'country', 'status', 'height(m)', 'height(ft)', 
                                  'floors', 'completion', 'material', 'use'])
file_name = str(region) + ".csv"
df.to_csv(file_name)

driver.close()
    