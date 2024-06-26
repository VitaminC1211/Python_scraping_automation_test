from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get(url)

first_name = driver.find_element(By.XPATH, '//*[@id="input-firstname"]')

first_name.send_keys("First")

last_name = driver.find_element(By.XPATH, '//*[@id="input-lastname"]')

last_name.send_keys('Second')

email = driver.find_element(By.XPATH, '//*[@id="input-email"]')

email.send_keys('rabit.cr257@gmail.com')

telephone =  driver.find_element(By.XPATH, '//*[@id="input-telephone"]')

telephone.send_keys("+123-456-789")

password = driver.find_element(By.XPATH, '//*[@id="input-password"]')

password.send_keys('yourPassword')

password_confirm = driver.find_element(By.XPATH, '//*[@id="input-confirm"]')

password_confirm.send_keys('yourPassword')

newsletter_subscribe = driver.find_element(By.XPATH, '//*[@id="content"]/form/fieldset[3]/div/div/div[2]/label')

newsletter_subscribe.click()

agree = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/div/label')

agree.click()

continue_button = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/input')

continue_button.click()

driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

sleep(5)

