"""
Collecting data from Trello

Jan 04 2016
Jon V

READ https://github.com/plish/Trolly for setting up your developer keys
"""

from datetime import datetime
import time
import trolly
import schedule
import config

def get_trello_data():
    client = trolly.client.Client(config.TRELLO_KEY, config.TRELLO_TOKEN)

    Board = None
    for board in client.get_boards():
        if board.id == config.BOARD_ID:
            Board = board
            break

    #DateTime, Name, LenOfTasks
    with open("data.csv", "a+") as f:
        for t_list in Board.get_lists():
            for card in t_list.get_cards():
                f.write("%s, %s, %s %s\n" % (datetime.now(), t_list.name, card.id, card.name))


schedule.every().day.at("23:45").do(get_trello_data)
while True:
    schedule.run_pending()
    time.sleep(10)
