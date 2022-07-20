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

    for ul_tag in soup.find_all("tr"): 
        td_tags= ul_tag.find_all("td")
        temp_list = []
            
        for j in td_tags:
            temp_list.append(j.text.rstrip())
        

    star_data.append(temp_list)
    
    
    with open("scraper.csv","w") as file:
        writer= csv.writer(file)
        writer.writerow(headers)
        writer.writerows(star_data)
    
scrape()

# df= pd.DataFrame(list(zip(list1,list2,list3,list4)), columns= ["column1", "column2","column3", "column4"])
# df.to_csv("name.csv")
