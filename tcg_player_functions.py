from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TcgPlayer:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.card_search_results = []

    def start_session(self):
        self.driver.get("http://www.tcgplayer.com")
        self.driver.find_element(By.XPATH, '/html/body').click()
        time.sleep(5)
        # close popup box that appears
        self.driver.find_element(By.ID, "dfwid-close-225931").click()

    def debug(self):
        print("debug")

    def get_search_bar(self):
        # accessing the search bar appears to be slow for some reason, maybe due to the autocomplete function on the site.  Loop is to keep searching for it till it is found.
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

    def search_for_card(self, card, card_set):
        # first select the search bard and then enter the card name
        search_bar = self.get_search_bar()
        search_bar.click()
        search_bar.clear()
        search_bar.send_keys(card)
        search_bar.send_keys(Keys.ENTER)
        self.get_search_results()
        card_price = self.get_card_price(card_set)

        # return (card, card_set, card_price)
        return {
            "card_name": card,
            "card_set": card_set,
            "card_price": card_price
        }

    def select_card_set(self, card_set):
        search_result_sets = [item.find_element(By.CSS_SELECTOR, "span.search-result__subtitle").text.lower() for item in self.card_search_results]
        # print(search_result_sets)
        # print(card_set)
        if card_set in search_result_sets:
            return search_result_sets.index(card_set)


    def get_search_results(self):
        time.sleep(1)
        # print(self.driver.find_elements(By.CSS_SELECTOR, "div.search-result"))
        setattr(self, "card_search_results",self.driver.find_elements(By.CSS_SELECTOR, "div.search-result"))
        # self.card_search_results = self.driver.find_elements(By.CSS_SELECTOR, "div.search-result")
        # print(self.card_search_results)

    def get_card_price(self, card_set):
        set_index = self.select_card_set(card_set)
        retry_count = 0
        run = True
        while run == True:
            try:
                # time.sleep(0.5)
                card_price = self.card_search_results[set_index].find_element(By.CSS_SELECTOR, "span.search-result__market-price--value").text
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