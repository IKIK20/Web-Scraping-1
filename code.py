from selenium import webdriver
from bs4 import BeautifulSoup
import csv

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("./chromedriverc")
browser.get(start_url)

import time
time.sleep(10)

def scrape():
    headers = ["Name", "Distance", "Mass", "Radius"]
    star_data = []

    soup= BeautifulSoup(browser.page_source, "html.parser")
        #temp_25_list = []
    star_table = soup.find('table')
    star_table.find_all('tr')

    for ul_tag in soup.find_all("tr"): 
        td_tags= ul_tag.find_all("td")
        temp_list = []
            
        for j, td_tag in enumerate(td_tags):
            if j==0:
                temp_list.append(td_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(td_tag.contents[0])
                except:
                    temp_list.append("")

    star_data.append(temp_list)
    browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    verify= False
    
    
    with open("scraper.csv","w") as file:
        writer= csv.writer(file)
        writer.writerow(headers)
        writer.writerows(star_data)
    
scrape()