from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
browser = webdriver.Chrome('/Users/nirvikkasula/Documents/Coding/Projects/Project 127 and 128/env/chromedriver')
browser.get(start_url)
time.sleep(15)
headers = ['Star_name','Distance','Mass','Radius']
star_data = []
new_star_data = []
soup = BeautifulSoup(browser.page_source, 'html.parser')
def scrape():
    for i in range(0,439):
        for ult in soup.find_all('ul',attrs = {'class','star'}):
            litags = ult.find_all('li')
            tempList = []
            for index,litag in enumerate(litags):
                if (index == 0):
                    tempList.append(litag.find_all('a')[0].contents[0])
                else:
                    try:
                        tempList.append(litag.contents[0])
                    except:
                        tempList.append('')

            star_data.append(tempList)

scrape()



with open('final_scrapping.csv','w') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(star_data)