
from bs4 import BeautifulSoup
import time
import json
import time
from datetime import datetime
import requests
import lxml
import random

import re
import cssutils

import selenium as sm

all_data=[]
all_data_demo=[]

print("RUNNING... ")



#
#
# print(" TEST  ")
# link='https://www.flipkart.com/joy-honey-almonds-nourishing-skin-cream-500-ml/p/itmeh2whvhc4uabc?pid=MSCEH2WHFPNEU3KB&lid=LSTMSCEH2WHFPNEU3KBZ5IDZJ&marketplace=FLIPKART&srno=b_1_2&otracker=browse&fm=organic&iid=en_P%2Bvj1A0CkbARTRXcMFXlsWLo9QdQzX1rK%2BDPA%2BOX39s56HRfonVkEQnyNQgo2mKQfvdLhP4JNQR1fPaAk7F%2BGQ%3D%3D&ppt=browse&ppn=browse&ssid=5i8spbwrgns7cydc1575019771471'
#
#
#
#
# form_data = {
#
#     'value':'700001'
#
#     }
#
# response = requests.post(link, data=form_data)
# print(response.text)
#
# individual_page = requests.get(link)
# if individual_page.status_code == requests.codes.ok:
#     bs = BeautifulSoup(individual_page.text, 'lxml')
#     time.sleep(1)
#     name=bs.findAll('div',attrs={'class':'_3BTv9X _3iN4zu'})
#     #print(name)
#     # soup = BeautifulSoup(link.text, 'html.parser')
#
#     script = bs.find(id='jsonLD')
#     image_json = json.loads(script.text)
#     for obj in image_json:
#         if obj['@type'] == 'Product':
#             url = obj['image']
#
#     print(url)
#

# print(" 1 1 ")

link1="https://www.flipkart.com/ponds-triple-vitamin-moisturizing-lotion/p/itmdfhtzxbau4vff?pid=MSCDFHSJXZZVJPED&lid=LSTMSCDFHSJXZZVJPEDI1P539&marketplace=FLIPKART&srno=b_1_4&otracker=browse&fm=organic&iid=3daa0bf8-60d9-4a7c-9ccf-cc6b6381b1eb.MSCDFHSJXZZVJPED.SEARCH&ppt=browse&ppn=browse&ssid=d4z7jnkw39g8vh1c1577471263435"


# page = requests.get(link1)
# if page.status_code == requests.codes.ok:
#     bs = BeautifulSoup(page.text, 'lxml')
#     obj2=bs.findAll('ul',attrs={'class':'fUBI-_'})
#     print(len(obj2))
#     obj3 = bs.findAll('div', attrs={'class': '_2h52bo _15sV4W _3xOS0O'})
#     if len(obj3)==0:
#         print("NULL")
#
#
# print(" 2 2 ")

link2="https://www.flipkart.com/vaseline-intensive-care-deep-restore-body-lotion/p/itmf7he7ngxgchwb?pid=MSCED33TFGDWGF3B&lid=LSTMSCED33TFGDWGF3BCRUCPL&marketplace=FLIPKART&spotlightTagId=BestsellerId_g9b%2Fema%2F5la&srno=b_1_3&otracker=browse&fm=organic&iid=364bd2cf-73e6-497f-af51-e25ab871f853.MSCED33TFGDWGF3B.SEARCH&ppt=browse&ppn=browse&ssid=mq51jbxgtzap68741577546260993"

# page = requests.get(link2)
# if page.status_code == requests.codes.ok:
#     bs = BeautifulSoup(page.text, 'lxml')
#     obj2=bs.findAll('ul',attrs={'class':'fUBI-_'})
#     for i in obj2:
#         for j in range(len(i.findAll('a'))):
#             a='https://www.flipkart.com'+i.findAll('a')[j]['href']
#             print("1 ",a)
#             # a = i.findAll('a')[1]['href']
#             # print("2 ",a)
#             # print(i.findAll('a')[0]['href'])
#
#
#     obj3 = bs.findAll('div', attrs={'class': '_2h52bo _15sV4W _3xOS0O'})
#     print(obj3[0].text)
#     for i in obj3:
#         print(i.text)
#

flipcart_main_url = 'https://www.flipkart.com'
product_urls=[]
all_product_urls=[]
search_url = f'https://www.flipkart.com/beauty-and-grooming/body-face-skin-care/body-and-face-care/pr?sid=g9b%2Cema%2C5la&p%5B%5D=facets.ideal_for%255B%255D%3DMen%2B%2526%2BWomen&otracker=categorytree&p%5B%5D=facets.ideal_for%255B%255D%3DWomen&p%5B%5D=facets.ideal_for%255B%255D%3DUnisex&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&otracker=nmenu_sub_Women_0_Skin%20Care'

product_urls.append(search_url)

next_search_url = 'https://www.flipkart.com/beauty-and-grooming/body-face-skin-care/body-and-face-care/pr?sid=g9b%2Cema%2C5la&p%5B%5D=facets.ideal_for%255B%255D%3DMen%2B%2526%2BWomen&p%5B%5D=facets.ideal_for%255B%255D%3DWomen&p%5B%5D=facets.ideal_for%255B%255D%3DUnisex&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&otracker=nmenu_sub_Women_0_Skin+Care&page=2'
product_urls.append(next_search_url)



#Gatheing main page urls
time1 = datetime.now()

def gather_urls(search_url):
    page = requests.get(search_url)
    if page.status_code == requests.codes.ok:
        bs = BeautifulSoup(page.text, 'lxml')
    next_page_link = bs.findAll('a', attrs={'class': '_3fVaIS'})
    if len(next_page_link )!=0:
        next_page_link = flipcart_main_url + next_page_link[1]['href']
        # print("**********NEXT PAGE LINK******** ", next_page_link)
        product_urls.append(next_page_link)
        gather_urls(next_page_link)
    if len(next_page_link)== 0:
        pass

gather_urls(next_search_url)

##Getting urls of the main page
product_urls = product_urls[:-1]
print("Product URLS ", product_urls)

#next_search_url='https://www.flipkart.com/beauty-and-grooming/body-face-skin-care/body-and-face-care/pr?sid=g9b%2Cema%2C5la&p%5B%5D=facets.ideal_for%255B%255D%3DMen%2B%2526%2BWomen&p%5B%5D=facets.ideal_for%255B%255D%3DWomen&p%5B%5D=facets.ideal_for%255B%255D%3DUnisex&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&otracker=nmenu_sub_Women_0_Skin+Care&page=2'
time2 = datetime.now()

def get_product_name_links(url):
    page = requests.get(url)
    if page.status_code == requests.codes.ok:
        bs = BeautifulSoup(page.text, 'lxml')
        name_link = bs.findAll('a', attrs={'class': '_2cLu-l'})

    for a in name_link:
        all_product_urls.append(flipcart_main_url + a['href'])


### This loop takes the main page urls and collect teh name and links of all products

for product_number in range(len(product_urls)):
    i=product_urls[product_number]
    get_product_name_links(i)

time3 = datetime.now()


print("ALL PRODUCTS URLS ",all_product_urls)
print("ALL PRODUCTS URLS Length ",len(all_product_urls))







def bring_all_data():
    k=0
    for link in all_product_urls:
        scraped_data = {}
        variation=[]
        product_variation={}
        k = k + 1
        random_number=random.randrange(100,300)
        tt=random.randrange(5,15)
        if k%random_number==0:
            time.sleep(tt)
        print("REQUEST NO  ", k)
        individual_page = requests.get(link)
        if individual_page.status_code == requests.codes.ok:
            bs = BeautifulSoup(individual_page.text, 'lxml')
            name = bs.findAll('span', attrs={'class': '_35KyD6'})
            for n in name:
                name = n.text
            scraped_data['name'] = name
            # print("1")
            # print(scraped_data)
            scraped_data['product_link'] = link
            # print("2")
            # print(scraped_data)
            original_price = bs.findAll('div', attrs={'class': '_3auQ3N _1POkHg'})
            for o in original_price:
                original_price = o.text
            scraped_data['original_price'] = original_price
            # print("3")
            # print(scraped_data)
            # print("Original Price ", original_price)
            discounted_price = bs.findAll('div', attrs={'class': '_1vC4OE _3qQ9m1'})
            for d in discounted_price:
                discounted_price = d.text
            scraped_data['discounted_price'] = discounted_price
            # print("discounted_price ", discounted_price)
            # print("4")
            # print(scraped_data)
            image_link = bs.findAll('div', attrs={'class': '_2_AcLJ'})
            # print("LEN ", len(image_link))
            script = bs.find(id='jsonLD')
            image_json = json.loads(script.text)
            for obj in image_json:
                if obj['@type'] == 'Product':
                    url = obj['image']
            # print(url)
            scraped_data['main_image']=url
            scraped_data['side_image'] = []
            if len(image_link) != 0:
                for i in range(len(image_link)):
                    image1 = image_link[i]['style']
                    image1 = image1.replace('background-image:url(', '').replace(')', '')
                    scraped_data['side_image'].append(image1)
                    print(scraped_data['side_image'])
            else:
                scraped_data['side_image'].append("NULL")

            list_of_variation={}
            product_variation_urls=[]

            is_there_any_variations = bs.findAll('ul', attrs={'class': 'fUBI-_'})

            if len(is_there_any_variations)==0:
                list_of_variation='NULL'
                scraped_data['variation']=list_of_variation
            if len(is_there_any_variations)!=0:
                for i in is_there_any_variations:
                    for j in range(len(i.findAll('a'))):
                        urls_to_scrap_for_variation = 'https://www.flipkart.com' + i.findAll('a')[j]['href']
                        product_variation_urls.append(urls_to_scrap_for_variation)
            print(" TEST TEST TEST ")
            list = []
            print("PRODUCT variation urls ",product_variation_urls)

            if len(product_variation_urls)!=0:
                k=0
                for link in product_variation_urls:

                    individual_page = requests.get(link)
                    if individual_page.status_code == requests.codes.ok:
                        bs = BeautifulSoup(individual_page.text, 'lxml')
                        name = bs.findAll('span', attrs={'class': '_35KyD6'})
                        print("NAMEEEEE ",name)
                        for n in name:
                            name = n.text
                        list_of_variation['name'] = name
                        list_of_variation['product_link']=link
                        print("LINKKKK ",link)
                        quantity = bs.findAll('div', attrs={'class': '_2h52bo _15sV4W _3xOS0O'})
                        if len(quantity)!=0:
                            print("BEFORE K ",k )
                            list_of_variation['quantity']= quantity[k].text
                            k=k+1
                            print("K= ", k)
                        original_price = bs.findAll('div', attrs={'class': '_3auQ3N _1POkHg'})
                        for o in original_price:
                            original_price = o.text
                        print("ORIGINAL PRICE ", original_price)
                        list_of_variation['original_price'] = original_price

                        discounted_price = bs.findAll('div', attrs={'class': '_1vC4OE _3qQ9m1'})
                        for d in discounted_price:
                            discounted_price = d.text
                        print("DISCOUNTTTTTT ",discounted_price)
                        list_of_variation['discounted_price'] = discounted_price

                        image_link = bs.findAll('div', attrs={'class': '_2_AcLJ'})
                        script = bs.find(id='jsonLD')
                        image_json = json.loads(script.text)
                        for obj in image_json:
                            if obj['@type'] == 'Product':
                                url = obj['image']
                        print("MAIN IMAGEEEEEE ",url)
                        list_of_variation['main_image'] = url
                        list_of_variation['side_image'] = []
                        if len(image_link) != 0:
                            for i in range(len(image_link)):
                                image1 = image_link[i]['style']
                                image1 = image1.replace('background-image:url(', '').replace(')', '')
                                list_of_variation['side_image'].append(image1)

                        else:
                            list_of_variation['side_image'].append("NULL")
                    print("LIST OF variation ",list_of_variation)
                    print("BEFORE APPEND ", list)
                    list.append(list_of_variation)
                    print("After  APPEND ", list)
                    list_of_variation={}
                    print("LIST LIST ",list)

            scraped_data['variation']=list
            print("SCRAPPED data ",scraped_data)
            #print(" TEST TEST TEST ")
            all_data.append(scraped_data)
            #print("FFFFFFFFFFFFFFFFFF",scraped_data)
            with open("flip_data.json", "w", encoding='utf8') as writeJSON:
                json.dump(all_data, writeJSON, ensure_ascii=False)

bring_all_data()




with open("flip_data.json", "w",encoding='utf8') as writeJSON:
   json.dump(all_data, writeJSON, ensure_ascii=False)

print(all_data)




time4 = datetime.now()


