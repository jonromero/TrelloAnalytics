"""
Collecting data from Trello

Jan 04 2016
Jon V

READ https://github.com/plish/Trolly for setting up your developer keys
"""

import trolly
from datetime import datetime

# sudo pip install Trolly
TRELLO_KEY = 'YOUR_KEY'
TRELLO_TOKEN = 'YOUR_TOKEN'
BOARD_ID = 'YOUR_BOARD_ID'

client = trolly.client.Client(TRELLO_KEY, TRELLO_TOKEN)

Board = None
for board in client.get_boards():
    if board.id == BOARD_ID:
        Board = board
        break

#DateTime, Name, LenOfTasks
for t_list in Board.get_lists():
    print "%s, %s, %s" % (datetime.now(), t_list.name, len(t_list.get_cards()))





