import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver_path = "./chromedriver-linux64/chromedriver"
serv_path = Service(driver_path)
driver = webdriver.Chrome(service = serv_path)
driver.get("https://arpanpariyar.com.np/")
hire_me = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"btn-hireme")))
hire_me.click()
user_name = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME, "your-name")))
user_name.send_keys("Alok Shrestha")
email_adress = WebDriverWait(driver ,10).until(EC.visibility_of_element_located((By.NAME, "your-email")))
email_adress.send_keys("alokshrestha12386@gmail.com")
project_name = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"project-name")))
project_name.send_keys("automation")
project_type = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"project-type")))
project_type.click()
# project_type_1 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.TAG_NAME,"select>option")))
select = Select(project_type)
select.select_by_visible_text("Video Editing")
budget_type = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"budget-range")))
budget_type.click()
select_1 = Select(budget_type)
select_1.select_by_visible_text(("$250-$500"))
project_brief = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"project-brief")))
project_brief.send_keys("hello arpan")
time.sleep(20)
send_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"wpcf7-submit")))
send_button.click()
time.sleep(20)




