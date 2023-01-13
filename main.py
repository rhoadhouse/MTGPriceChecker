from tcg_player_functions import TcgPlayer

# start session for scraping tcgplayer.com
tcg_driver = TcgPlayer()
tcg_driver.start_session()


# Open the cards to search and save all as a list

with open("Cards_to_search.txt") as file:
    contents = file.readlines()
    cards = [card[0:card.index(",")] for card in contents]
    cards = []
    card_sets = []
    card_data = []
    for item in contents:
        try:
            card = item[0:item.index(",")]
        except:
            card = ""
        try:
            card_set = item[item.index(",")+1:item.index("\n")].replace(" ","")
        except:
            card_set = ""
        card_data.append({
            "card": card,
            "card_set": card_set
        })

    print(card_data)

# search for all cards in list
for item in card_data:
    tcg_driver.search_for_card(item["card"])
    tcg_driver.select_card_set(item["card_set"])

tcg_driver.quit()