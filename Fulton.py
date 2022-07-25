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
  
csv_data_num = read_data_from_csv('/Users/christianmcalpine/Desktop/Fultonsplit.csv')

for line in csv_data_num:
    driver = webdriver.Chrome("/Users/christianmcalpine/Desktop/chromedriver")
    driver.get('https://iaspublicaccess.fultoncountyga.gov/search/commonsearch.aspx?mode=address')
    driver.find_element_by_xpath('//*[@id="btAgree"]').click()
    #Input street number
    csv_data_query = driver.find_element_by_xpath('//*[@id="inpNumber"]')
    csv_data_query.send_keys(line[0])
    #Input street name
    csv_data_query = driver.find_element_by_xpath('//*[@id="inpStreet"]')
    csv_data_query.send_keys(line[1])
    
    csv_data_query.send_keys(Keys.RETURN)
    
    #Select top result   
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    
    no_result_loc = soup.find('div', {'class': 'contentpanel'})
    no_result = no_result_loc.find_all('span')[0].get_text()
    if no_result == 'Results':
        
        driver.find_element_by_xpath('//*[@id="searchResults"]/tbody/tr[3]/td[3]').click()
        time.sleep(1)
    
        #Last sales date
        driver.find_element_by_xpath('//*[@id="sidemenu"]/li[2]/a').click()
        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')
    
        sales_date_loc = soup.find('div', {'class': 'holder'}).get_text()
        if sales_date_loc == "\n-- No Data --\n":
            print('n.d.')
        else:
            sales_date_loc = soup.find('div', {'class': 'holder'})
            sales_date = sales_date_loc.find_all('tr')[2]
            sales_date_yes = sales_date.find_all('td')[0].get_text()
            print(sales_date_yes)
        
        time.sleep(1)
        
        driver.find_element_by_xpath('//*[@id="sidemenu"]/li[5]/a').click()
        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')
        
        permits_loc = soup.find('div', {'class': 'holder'}).get_text()
        if permits_loc == "\n-- No Data --\n":
            print('No permits')
        else:
            permits_loc = soup.find('div', {'class': 'holder'})
            permits = permits_loc.find_all('table')[1]
            permits_yes = permits.find('tbody')
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
