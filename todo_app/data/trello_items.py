#from flask import session
import requests
import json

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]

def get_items(BOARD_ID,APIKey,APIToken):
    """
    Fetches all saved items from trello board_id.

    Args:
        id: The BOARD_ID of the trello board and API_KEY, API_TOKEN.

    Returns:
        list: The list of cards from a list/board.
    """
    query = {
        'key': APIKey,
        'token': APIToken,
        'cards': 'open'
    }

    print(query)
    #url = "https://api.trello.com/1/boards/" + BOARD_ID + "/cards"
    url = "https://api.trello.com/1/boards/" + BOARD_ID + "/lists"
    print(url)
    response = requests.request("GET",url,params=query)

    jsonResponse = response.json()
    items=[]
    
    # add try abort response errors i.e. server code 500
    #

    print(jsonResponse)

    id_number=1
    for lists in jsonResponse:
        print(lists['id'])
        print(lists['name'])
        for card in lists['cards']:
            print(card['name'])
            if lists['name'] == 'Doing':
                status="Started"
            else:
                status="Not Started"

            getitem = {'id': id_number, 'title': card['name'], 'status': status}
            items.append(getitem)
            id_number += 1

    return items


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items(app.config["BOARD_ID"],app.config["API_KEY"],app.config["API_TOKEN"])

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    items.append(item)
    #################session['items'] = items

    return item