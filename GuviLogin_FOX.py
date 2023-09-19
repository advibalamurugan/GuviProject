import selenium.webdriver as webdriver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Bala:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()
        self.username = 'Admin'
        self.password = 'admin123'
        self.firstName = 'Vani'
        self.middleName = 'B'
        self.lastName = 'Balasubramanian'

# usage of NAME & XPATH
    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(20)
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.password)
        self.driver.find_element(by=By.XPATH,
value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Add ']"))).click()
        sleep(20)
        self.driver.find_element(by=By.NAME, value='firstName').send_keys(self.firstName)
        self.driver.find_element(by=By.NAME, value='middleName').send_keys(self.middleName)
        self.driver.find_element(by=By.NAME, value='lastName').send_keys(self.lastName)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Save ']"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Employee List']"))).click()
        elem = WebDriverWait(browser, 120, 1).until(expect.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Search ']"))).click()
url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
Bala(url).login()