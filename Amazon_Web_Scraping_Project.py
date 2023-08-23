#--------Amazon web scraping project
#--------Getting data from amazon website and exporting the data into a csv file 

#--------importing libraries
import requests as rq
import pandas as pd
from bs4 import BeautifulSoup as bs

#---------amazon website url 
url="https://www.amazon.in/s?k=asus+tuf+a15&crid=RL4LRXJZM2S0&sprefix=%2Caps%2C3868&ref=nb_sb_ss_recent_1_0_recent"

#---------creating connection/response
page=rq.get(url,headers=Headers)
#---------parsing the data into html format
soup=bs(page.content,"html.parser")
#---------creating a table using pandas datagrame
#---------initializing column title values
df=pd.DataFrame(columns=["Product Name","Prize","Specs","Rating","Total Ratings"])
#---------searching the "div" which contain required datas and asssigning it
fullpage=soup.find_all(class_="sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 sg-col-12-of-24 s-list-col-right")

#---------function to scrap the product name
def get_productname():
        product=fullpage[i].find(class_="a-size-medium a-color-base a-text-normal")
        product_name=product.text.split(",",1)[0]
        return product_name

#---------function to derive the product prize 
def get_specs():
        specs=fullpage[i].find(class_="a-size-medium a-color-base a-text-normal")
        specs_detail=specs.text.split(",",1)[1]
        order_specs=specs_detail.replace(",","\n")
        return order_specs

#---------function to  derive the product specification 
def get_prize():
        prize=fullpage[i].find(class_="a-price-whole")
        prize_n=prize.text
        return prize_n

#---------function to scrap the product ratings
def get_ratings():
        rating=fullpage[i].find(class_="a-icon-alt")
        rating_n=rating.text.split()[0]
        return rating_n

#---------function to derive total ratings
def get_totalratings():
        totalr=fullpage[i].find(class_="a-size-base s-underline-text")
        total_rat=totalr.text.strip("()")
        return total_rat

#loopinf through each div within the assigned div untill the length of the div
i=0
while i <len(fullpage):

#excepting error from the div if it does not contain required data
    try:

#calling each function ,passing position of div as parameter
        product_nm=get_productname(i)
        prize_dt=get_prize(i)
        specs_dtl=get_specs(i)
        ratings_str=get_ratings(i)
        total_rtngs=get_totalratings(i)

#----------adding the data of each object into the dataframe row wise
        data=[product_nm,prize_dt,specs_dtl,ratings_str,total_rtngs]

#----------getting length of the dataframe to get the last position for appending
        pos=len(df)
        df.loc[pos]=data
        i+=1

#--------accepting error msg from div which doesnt contain the data and skipping to next div
    except:
        print("error")
        i+=1

#--------exporting the 
df.to_csv(R"C:\Users\Desktop\AMAZON_LAPTOP_DATA.CSV")

#--------printing dataframe
print(df)
