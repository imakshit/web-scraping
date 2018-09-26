import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=&find_loc="
loc = "Newport Beach, CA" #set the location
page = 10 #set the page number

url = base_url + loc + "&start" + str(page) #main url

yelp_r = requests.get(url)
yelp_soup = BeautifulSoup(yelp_r.text , 'html.parser')

#print(yelp_r.status_code) #status

bussinesses = yelp_soup.findAll('div' , {'class': 'biz-listing-large'})

for biz in bussinesses: 
    title = biz.findAll('a', {'class':'biz-name'})[0].text
    print(title)
    address=biz.findAll('address')[0]
    print(address)
    print("\n")
    phone = biz.findAll('span', {'class':'biz-phone'})[0].text
    print(phone)
