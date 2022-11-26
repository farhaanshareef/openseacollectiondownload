import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.chrome.service import Service

#creating a directory to save images
folder_name = 'openseaimages2'
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

def download_image(url, folder_name, num):

    # write image to file
    reponse = requests.get(url)
    if reponse.status_code==200:
        with open(os.path.join(folder_name, str(num)+".jpg"), 'wb') as file:
            file.write(reponse.content)

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s)

search_URL = "https://opensea.io/collection/drippies-solana"
driver.get(search_URL)
driver.maximize_window()


a = input("Waiting...")

#Scrolling all the way up
driver.execute_script("window.scrollTo(0, 0);")

page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
containers = pageSoup.findAll('div', {'class':"sc-f087f95e-0 sc-f087f95e-1 gwpnfr gyivza AssetMedia--img"})

print(len(containers))

len_containers = len(containers)

for i in range(1, len_containers+1):
    j=1
    while j < len_containers:

        #imageElement = driver.find_elements(By.CLASS_NAME, "iDCpHK")

        imageElement = driver.find_element(By.XPATH, """//*[@id="main"]/div/div/div/div[5]/div/div[3]/div[3]/div[3]/div[3]/div/div[""" + str(i) + """]/article/a/div[1]/div/div/div/div/span/img""")
        imageURL= imageElement.get_attribute('src')
        break

    # Downloading image
    try:
        download_image(imageURL, folder_name, i)
        print("Downloaded element %s out of %s total. URL: %s" % (i, len_containers + 1, imageURL))
    except:
        print("Couldn't download an image %s, continuing downloading the next one" % (i))
