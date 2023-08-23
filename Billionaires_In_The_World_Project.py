#------web scraping data about "Top1 00 Billionairs in the world" from the site to the csv file 
#------------importing libraries
import requests,pandas
from bs4 import BeautifulSoup as bs

#------------website url 
url="https://ceoworld.biz/2023/03/04/the-worlds-richest-people-top-billionaires-2023/"

#------------creating connection and response
page =requests.get(url)

#------------formatting acquired data content into html format 
soup=(bs(page.text,features='html.parser'))

#------------structure formatting
soup.prettify()

#-----------finding "div" 
title=(soup.find("tr"))

#-----------selcting table title data
title_data=[i.text for i in title.find_all("th")]

#------------creating pandas dataframe and initializing column title with extracted values 
df=pandas.DataFrame(columns=title_data)
#print(df)

#-------------extracting row values
rows=(soup.find_all("tr")[1:101])
#-------------looping through the extracted row data
for i in rows:
   
   #--------------taking the content of the data
   rowdata=[j.text for j in i.find_all("td")]
   #--------------getting the length of the dataframe table
   pos=len(df)
   #--------------appending the data to the next position of the table
   df.loc[pos]=rowdata

#-------------------viewing the dataframe
print(df)

#---------------exporting the dataframe into a csv file without the index column
df.to_csv(r"C:\Users\Desktop\List_Of_Billionaires.csv",index=False) 
