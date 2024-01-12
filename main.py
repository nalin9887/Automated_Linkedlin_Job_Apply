import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
data=driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3770421222&f_AL=true&geoId=101716408&keywords=python%20developer&location=Jaipur%2C%20Rajasthan%2C%20India&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")
sign_in=driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
sign_in_mail=driver.find_element(By.XPATH,'//*[@id="username"]')
sign_in_mail.send_keys("6377864136")

sign_in_pass=driver.find_element(By.XPATH,'//*[@id="password"]')
sign_in_pass.send_keys("Nalin@9887")

sign_in_button=driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()
easy_apply=driver.find_element(By.CSS_SELECTOR,".jobs-s-apply button")
easy_apply.click()
submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".display-flex button")
submit_button.click()
time.sleep(2)
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button Continue ")
submit_button.click()
time.sleep(30)

