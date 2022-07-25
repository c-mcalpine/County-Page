from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import csv
import pandas as pd

def read_data_from_csv(filename):
    datalist = []
    csvdata = open(filename, 'r')
    reader = csv.reader(csvdata)
    next(reader)
    for rows in reader:
        datalist.append(rows)
    datalist = [item[:2] for item in datalist]
    return datalist
    
csv_data_num = read_data_from_csv('--filepath--')

for line in csv_data_num:
    driver = webdriver.Chrome("--filepath--")
    driver.get('--page--')
    driver.find_element_by_xpath('--agreepage--"]').click()
    #Input street number
    csv_data_query = driver.find_element_by_xpath('--xpath--')
    csv_data_query.send_keys(line[0])
    #Input street name
    csv_data_query = driver.find_element_by_xpath('--xpath--')
    csv_data_query.send_keys(line[1])
    
    csv_data_query.send_keys(Keys.RETURN)
    
    #Select top result   
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    
    no_result_loc = soup.find('div', {'class': '--input--'})
    no_result = no_result_loc.find_all('--input--').get_text()
    if no_result == 'Results':
        
        driver.find_element_by_xpath('--xpath--').click()
        time.sleep(1)
    
        #Last sales date
        driver.find_element_by_xpath('--xpath--').click()
        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')
    
        sales_date_loc = soup.find('div', {'class': '--input--'}).get_text()
        if sales_date_loc == "\n-- No Data --\n":
            print('n.d.')
        else:
            sales_date_loc = soup.find('div', {'class': '--input--'})
            sales_date = sales_date_loc.find_all('--input--')[2]
            sales_date_yes = sales_date.find_all('--input--')[0].get_text()
            print(sales_date_yes)
        
        time.sleep(1)
        
        driver.find_element_by_xpath('--input--').click()
        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')
        
        permits_loc = soup.find('div', {'class': '--input--'}).get_text()
        if permits_loc == "\n-- No Data --\n":
            print('No permits')
        else:
            permits_loc = soup.find('div', {'class': '--input--'})
            permits = permits_loc.find_all('--input--')[1]
            permits_yes = permits.find('--input--')
            #get_all_data(permits)
            df_p = pd.DataFrame(permits_yes) #columns = {'Permit #', 'Permit Date', 'Purpose', 'Amount'})
            header_p = df_p.iloc[0]
            df_p = df_p[1:]
            df_p.columns = header_p
            df_p.drop(df_p.tail(1).index, inplace = True)
            
            print(df_p)
        
    else:
        print("No data")
        
data_1 = [sales_join]
file = open('Fulton.csv', 'a+', newline = '')
with file:
    write = csv.writer(file)
    write.writerows(data_1)
