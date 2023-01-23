from tcg_player_functions import TcgPlayer

# start session for scraping tcgplayer.com
tcg_driver = TcgPlayer()
tcg_driver.start_session()


# Open the cards to search and save all as listed dictionary
with open("Cards_to_search.txt") as file:
    contents = file.readlines()
    cards = [card[0:card.index(",")] for card in contents]
    cards = []
    card_sets = []
    card_data = []
    for item in contents:
        try:
            card = str(item[0:item.index(",")])
        except:
            card = ""
        try:
            card_set = str(item[item.index(",")+1:item.index("\n")]).lower().strip()
        except:
            card_set = ""
        card_data.append({
            "card": card,
            "card_set": card_set,
            "card_price": ""
        })

    # print(card_data)

# search for all cards in list
data = [tcg_driver.search_for_card(card=item["card"],card_set=item["card_set"]) for item in card_data]

tcg_driver.quit()

try:
    f = open("Card Search Data.txt", "x")
    f.write("data")
    f.close()
except:
    f = open("Card Search Data.txt", "w")
    # clear data in the file
    f.write("")
    f.close()
    # reopen file with append privileges
    f = open("Card Search Data.txt", "a")
    for item in data:
        f.write(f"{item['card_name']},{item['card_set']},{item['card_price']}\n")
    f.close()
