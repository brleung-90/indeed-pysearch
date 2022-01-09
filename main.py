from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import *
import bs4

baseURL = "https://ca.indeed.com"

job_choice = input("Enter your job: ")
location_choice = input("Enter your location, leave blank to not specify location: ")

joblist = []

driver = webdriver.Chrome()
driver.get(baseURL)


def enter_():
    driver.set_window_size(1936, 1096)
    driver.find_element(By.ID, "text-input-what").send_keys(job_choice)
    driver.find_element(By.ID, "text-input-where").click()
    driver.find_element(By.ID, "text-input-where").send_keys(Keys.CONTROL + "a")
    driver.find_element(By.ID, "text-input-where").send_keys(Keys.DELETE)
    driver.find_element(By.ID, "text-input-where").send_keys(location_choice)
    driver.find_element(By.ID, "text-input-where").send_keys(Keys.ENTER)

    for body in driver.find_elements(By.TAG_NAME, 'h2'):
        print(body.text)


enter_()
