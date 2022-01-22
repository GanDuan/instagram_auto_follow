from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

path = PATH
username = NAME
password = PASSWORD
url = "https://www.instagram.com/"
people = "chefsteps"

class InstaFollower:
    def __init__(self):
        s = Service(path)
        self.driver = webdriver.Chrome(service=s)

    def login(self):
        self.driver.get(url)
        sleep(3)
        user_name = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        user_name.send_keys(username)
        pass_word = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
        pass_word.send_keys(password)
        pass_word.send_keys(Keys.ENTER)
        # sleep(5)
        # not_save = self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div/div/button")
        # not_save.click()
        # sleep(6)
        # nn_notification = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[3]/button[2]")
        # nn_notification.click()
        sleep(3)

    def find_followers(self, text):
        self.login()
        self.driver.get(f"{url}{text}/")

    def follow(self, text):
        self.find_followers(text)
        sleep(3)
        following = self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
        following.click()
        sleep(3)
        pop_up_window = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[3]")

        for i in range(NUMBER_YOU_WANT_TO_SCROLL):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight",
                pop_up_window)
            sleep(1)
        follow_button = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in follow_button:
            try:
                if button.text == "Following":
                    pass
                else:
                    button.click()
                    sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[2]")
                cancel_button.click()


instagram = InstaFollower()
instagram.follow(people)
