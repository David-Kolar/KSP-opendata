from selenium import webdriver
from selenium.webdriver.common.by import By

# Login data
login = "email@example.com"
password = "password"

# Open ksp webpage
driver = webdriver.Chrome()
driver.get("https://ksp.mff.cuni.cz/h/")

# Find and enter login page
element = driver.find_element(By.LINK_TEXT, "Přihlásit")
element.click()

# Enter login name
login_element = driver.find_element(By.XPATH, "/html/body/main/div[1]/div/form/table/tbody/tr[1]/td[2]/input")
login_element.send_keys(login)

# Enter password
password_element = driver.find_element(By.XPATH, "/html/body/main/div[1]/div/form/table/tbody/tr[2]/td[2]/input")
password_element.send_keys(password)

# Click
click_button = driver.find_element(By.XPATH, "/html/body/main/div[1]/div/form/p/input[2]")
click_button.click()