from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TcgPlayer:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def start_session(self):
        self.driver.get("http://www.tcgplayer.com")
        self.driver.find_element(By.XPATH, '/html/body').click()
        time.sleep(5)
        # close popup box that appears
        self.driver.find_element(By.ID, "dfwid-close-225931").click()

    def debug(self):
        print("debug")

    def get_search_bar(self):
        search = True
        while search == True:
            try:
                time.sleep(0.5)
                search_bar = self.driver.find_element(By.ID, "autocomplete-input")
                search_bar.click()
                search = False
            except:
                print("error")
        return search_bar

    def search_for_card(self, card):
        search_bar = self.get_search_bar()
        search_bar.click()
        search_bar.clear()
        search_bar.send_keys(card)
        search_bar.send_keys(Keys.ENTER)
        price = self.get_card_price()
        print(f"{card}, {price}")

    def get_card_price(self):
        retry_count = 0
        run = True
        while run == True:
            try:
                time.sleep(0.5)
                card_price = self.driver.find_element(By.CSS_SELECTOR, "span.search-result__market-price--value").text
                return card_price
            except:
                if retry_count > 5:
                    card_price = "error"
                    run = False
                    return card_price
                # print(retry_count)
                retry_count += 1
                # print("error")

    def quit(self):
        self.driver.quit()