# Trello card actions
#
import requests
import json
from todo_app.data.item import Item

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]

lists_ids=[]
items=[]

def get_items(BOARD_ID,APIKey,APIToken):
    """
    Fetches all saved items from trello board_id.

    Args:
        id: The BOARD_ID of the trello board and API_KEY, API_TOKEN.

    Returns:
        list: The list of cards from a list/board.
    """

    items=[]
    query = {
        'key': APIKey,
        'token': APIToken,
        'cards': 'open'
    }

    url = "https://api.trello.com/1/boards/" + BOARD_ID + "/lists"
    response = requests.request("GET",url,params=query)
    jsonResponse = response.json()

    # add try abort response errors i.e. server code 500
    #

    id_number=1
    for lists in jsonResponse: 
        lists_ids.append({'id': lists['id'], 'name': lists['name']})
        for card in lists['cards']:
            new_item = Item.from_trello_card(card,lists)
            items.append(new_item)
            id_number += 1

    return items

def add_item(title,BOARD_ID,APIKey,APIToken):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item,BOARD_ID,APIKey,APIToken.

    Returns:
        item: The saved item.
    """
    items = get_items(BOARD_ID,APIKey,APIToken)

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    items.append(item)

    for list_id in lists_ids:
        if list_id['name'] == 'To Do':
            created_in_list=list_id['id']
            break

    headers = {
        "Accept": "application/json"
    }

    query = {
        'idList': created_in_list,
        'key': APIKey,
        'token': APIToken,
        'name': title
    }
   
    url = "https://api.trello.com/1/cards"
    response = requests.request("POST",url,headers=headers,params=query)

    return item

def delete_item(Selected_item,BOARD_ID,APIKey,APIToken):
    """
    delete card using it's Selected_item, BOARD_ID, APIKey, APIToken.

    Args:
        The Trello card's Selected_item, BOARD_ID,APIKEY,APIToken.

    Returns:
        Nothing.
    """

    items = get_items(BOARD_ID,APIKey,APIToken)
    query = {   
        'key': APIKey,
        'token': APIToken
    }

    for findSelection in items:
        if findSelection['id'] == int(Selected_item):
            shortLink=findSelection['shortLink']
            url = "https://api.trello.com/1/cards/" + shortLink
            response = requests.request("DELETE",url,params=query)
            break

    return None


def completed_item(Selected_item,BOARD_ID,APIKey,APIToken):
    """
    completed card using it's shortLink and Done lists idList.

    Args:
        The Trello card's items id, BOARD_ID, APIKEY, APIToken.

    Returns:
        Nothing.
    """

    items = get_items(BOARD_ID,APIKey,APIToken)

    for Done_idList in lists_ids:
        if Done_idList['name'] == 'Done':
            break

    query = {
        'idList':  Done_idList['id'],   
        'key': APIKey,
        'token': APIToken
    }

    for findSelection in items:
        if findSelection['id'] == int(Selected_item):
            shortLink=findSelection['shortLink']
            url = "https://api.trello.com/1/cards/" + shortLink
            response = requests.request("PUT",url,params=query)
            break

    return None

def not_started_item(Selected_item,BOARD_ID,APIKey,APIToken):
    """
    switch card to not started status using it's shortLink and Done lists idList.

    Args:
        The Trello card's items id, BOARD_ID, APIKEY, APIToken.

    Returns:
        Nothing.
    """

    items = get_items(BOARD_ID,APIKey,APIToken)

    for Done_idList in lists_ids:
        if Done_idList['name'] == 'To Do':
            break

    query = {
        'idList':  Done_idList['id'],   
        'key': APIKey,
        'token': APIToken
    }

    for findSelection in items:
        if findSelection['id'] == int(Selected_item):
            shortLink=findSelection['shortLink']
            url = "https://api.trello.com/1/cards/" + shortLink
            response = requests.request("PUT",url,params=query)
            break

    return None