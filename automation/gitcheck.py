import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
ig_username = input("Enter your username:")
ig_password = input("Enter your password")

driver_path = "./chromedriver-linux64/chromedriver"
serv_path = Service(driver_path)
driver = webdriver.Chrome(service=serv_path)
driver.get("https://instagram.com")
username = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"username")))
username.send_keys(ig_username)
password = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"password")))
password.send_keys(ig_password)
login = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[3]")))

login.click()
not_login = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div")))
not_login.click()
message = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[5]/div/div/span/div/a/div")))
message.click()
notification_off = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")))
notification_off.click()
message_arpan = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span[text()='Bishnu Kandel']"))
)

message_arpan.click()
for i in range(1,10):

    real_message = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div")))
    real_message.click()
    real_message.send_keys("hello k xa")
    send = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[3]")))
    send.click()
time.sleep(10)


