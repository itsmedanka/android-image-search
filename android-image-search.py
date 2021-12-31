import pyshorteners
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import os
import pyshorteners as sh

print("open IP Webcam app and scan where to search")
print("REMEMBER TO BE IN SAME NETWORK OF YOUR LAPTOP!")
print("Welcome to android-image-search")
options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(options=options)
browser.get("http://192.168.0.72:8080/jsfs.html")
print("went to the site")
time.sleep(5)
os.system("rm image_search.png")#removes already saved file
time.sleep(2)
browser.save_screenshot("image_search.png")
print("got image")
time.sleep(3)
browser.get("https://www.google.com/imghp?hl=en")
print("went to the site")
time.sleep(2)
browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/span").click()
time.sleep(2)
browser_url = browser.current_url
browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/div[1]/div/a").click()
time.sleep(2)
browser.find_element(By.ID, "awyMjb").send_keys(os.getcwd()+"/image_search.png")
print("searching for image...")
for i in range(10):
    print("|", end='\r')
    time.sleep(0.2)
    print("/", end='\r')
    time.sleep(0.2)
    print("-", end='\r')
    time.sleep(0.2)
    print("\ ", end='\r')
    time.sleep(0.2)
time.sleep(5)
print(" ", end="\r")
if browser_url == browser.current_url:
    print("Image is hard to find")
else:
    print(pyshorteners.Shortener().tinyurl.short(browser.current_url))




