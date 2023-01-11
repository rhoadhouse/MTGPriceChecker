from tcg_player_functions import TcgPlayer

# start session for scraping tcgplayer.com
tcg_driver = TcgPlayer()
tcg_driver.start_session()


# Open the cards to search and save all as a list
with open("Cards_to_search.txt") as file:
    contents = file.readlines()
    cards = [card[0:card.index(",")] for card in contents]
    print(cards)

# search for all cards in list
for card in cards:
    tcg_driver.search_for_card(card)

tcg_driver.quit()