# Two browsers test for Google and Wikipedia with Waiting functional
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException, TimeoutException


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_ChSearch(self):
        driver_ch = self.driver
        driver_ch.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver_ch, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(3)
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_ch.title
        print(driver_ch.title + "is present on the page")
        driver_ch.find_element(By.XPATH, "//input[@id='g2-name']").clear()
        driver_ch.find_element(By.XPATH, "//input[@id='g2-email']").clear()
        driver_ch.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").clear()
        driver_ch.find_element(By.XPATH, "//input[@id='g2-name']").send_keys("Gulzat")
        driver_ch.find_element(By.XPATH, "//input[@id='g2-email']").send_keys("gigi@gmail.com")
        driver_ch.find_element(By.ID, "contact-form-comment-g2-message").send_keys("form filled out")
        driver_ch.find_element(By.XPATH, "//button[@class='pushbutton-wide']").submit()
        time.sleep(3)
        driver_ch.find_element_by_xpath("//a[contains(text(),'go back')]").send_keys(Keys.RETURN)

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            print("Go back is appeared")
        except TimeoutException:
            print("Finding took too much time!")

        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
            print("California Real Estate page is ready!")
        except ElementNotVisibleException:
            print("Element not found")

        time.sleep(3)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))
        time.sleep(3)
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_ch.title
        print(driver_ch.title + " is present on the page")

    def test_ChSearch2(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size(1120, 550)
        driver_chrome.get('https://qasvus.wordpress.com/')
        wait = WebDriverWait(driver_chrome, 3)
        wait.until(EC.visibility_of_element_located((By.ID, 'menu-item-116')))
        time.sleep(3)

    class FirefoxSearch(unittest.TestCase):

        def setUp(self):
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()

        def test_FirefoxSearch(self):
            driver_ff = self.driver
            driver_ff.get('https://qasvus.wordpress.com/')
            wait = WebDriverWait(driver_ff, 5)
            wait.until(EC.visibility_of_element_located((By.ID, "contact-form-comment-g2-message")))
            time.sleep(5)
            assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_ff.title
            print(driver_ff.title + " is present on the page")
            driver_ff.find_element(By.XPATH, "//input[@id='g2-name']").clear()
            driver_ff.find_element(By.XPATH, "//input[@id='g2-email']").clear()
            driver_ff.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").clear()
            driver_ff.find_element(By.XPATH, "//input[@id='g2-name']").send_keys("Gulzat")
            driver_ff.find_element(By.XPATH, "//input[@id='g2-email']").send_keys("gigi@gmail.com")
            driver_ff.find_element(By.ID, "contact-form-comment-g2-message").send_keys("form filled out")
            driver_ff.find_element(By.XPATH, "//button[@class='pushbutton-wide']").submit()
            time.sleep(5)
            driver_ff.find_element_by_xpath("//a[contains(text(),'go back')]").send_keys(Keys.RETURN)

            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
                print("Go back is appeared")
            except TimeoutException:
                print("Finding took too much time!")

            try:
                wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
                print("California Real Estate page is ready!")
            except ElementNotVisibleException:
                print("Element not found")

            time.sleep(5)

            wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))
            time.sleep(2)
            assert "California Real Estate – QA at Silicon Valley Real Estate" in driver_ff.title
            print(driver_ff.title + " is present on the page")

        def test_FirefoxSearch2(self):
            driver_firefox = self.driver
            driver_firefox.set_window_size(1250, 850)
            driver_firefox.get('https://qasvus.wordpress.com/')
            wait = WebDriverWait(driver_firefox, 5)
            wait.until(EC.visibility_of_element_located((By.ID, 'menu-item-116')))
            time.sleep(2)

        def tearDown(self):
            self.driver.quit()


