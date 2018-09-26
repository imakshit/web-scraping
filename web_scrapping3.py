import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=&find_loc="
loc = "Newport Beach, CA" #set the location
page = 10 #set the page number

url = base_url + loc + "&start" + str(page) #main url

yelp_r = requests.get(url)

print(yelp_r.status_code) #status

yelp_soup = BeautifulSoup(yelp_r.text , "html.parser")

print(yelp_soup.findAll('li' , {"class": 'regular-search-result'})) #fetch list items

for name in yelp_soup.findAll('a' , {"class": 'biz-name'}): #fetch data from biz-name
    print(name.text)
