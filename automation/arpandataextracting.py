import sys


# Now you can continue with the rest of your code

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import os
# Get the location of the chromedriver bundled with the executable
if getattr(sys, 'frozen', False):  # If the script is frozen (exe)
    chromedriver_path = os.path.join(sys._MEIPASS, 'chromedriver-linux64/chromedriver')
else:  # If running as a normal Python script
    chromedriver_path = '/home/alok/Downloads/chromedriver-linux64'


serv_path = Service(chromedriver_path)
driver = webdriver.Chrome(service=serv_path)

driver.get("https://koolarpan.com")
driver.maximize_window()

arpan_photo = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//img[@alt='Hi! I am Kool Arpan']")))
image_link = arpan_photo.get_attribute('src')

if image_link:
    data_folder = "/home/alok/Desktop/data_folder"
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    image_path = os.path.join(data_folder,"arpan_ko_photo.jpg")

    image_magnuparyoni = requests.get(image_link).content

    with open(image_path,'wb') as file:
        file.write(image_magnuparyoni)
    print(f"Image saved in {image_path}")
else:
    print("Image not found")


black_white = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//img[@class='attachment-perfect-portfolio-square size-perfect-portfolio-square wp-post-image']")))
black_white.click()
black_white_get = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//figure[@class='wp-block-video']//video")))
black_white_link = black_white_get.get_attribute('src')
if black_white_link:
    data_folder = "/home/alok/Desktop/data_folder"
    video_path = os.path.join(data_folder,"arpan_ko_video.mp4")
    video_req = requests.get(black_white_link).content
    with open(video_path,'wb') as file:
        file.write(video_req)
    print(f"Video saved in {video_path}")
else:
    print("video not found")
driver.quit()


