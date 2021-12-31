from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
from itertools import cycle

print("open IP Webcam app and scan where to search")
print("REMEMBER TO BE IN SAME NETWORK OF YOUR LAPTOP!")
print("Welcome to android-image-search")
options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox()
browser.get("http://192.168.0.72:8080/jsfs.html")
print("went to the site")
time.sleep(5)
browser.save_screenshot("image_search.png")
time.sleep(3)
browser.get("https://www.google.com/imghp?hl=en")
time.sleep(2)
browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/span").click()
time.sleep(2)
browser_url = browser.current_url
browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/div[1]/div/a").click()
time.sleep(2)
browser.find_element(By.ID, "awyMjb").send_keys("/home/yash/Python/image_search.png")
time.sleep(10)

if browser.current_url == browser_url:
    print("Loading...",end="\n")
    for i in cycle(["|", "/", "-", "\ "]):
        a = 0
        print(i, end='\r')
        time.sleep(0.2)
        if a > 10:
            print("image is hard to find")
            exit()

else:
        print(browser.current_url)




