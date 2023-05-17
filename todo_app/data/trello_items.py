# Trello card actions
#
import os
import requests
import json
from todo_app.data.item import Item

lists_ids=[]

#def get_items(BOARD_ID,APIKey,APIToken):
def get_items():
    """
    Fetches all saved items from trello board_id.

    Args:
        id: The BOARD_ID of the trello board and API_KEY, API_TOKEN.

    Returns:
        list: The list of cards from a list/board.
    """

    global BOARD_ID
    global APIKey
    global APIToken    

    BOARD_ID = os.environ.get('TRELLO_BOARD_ID')
    APIKey   = os.environ.get('TRELLO_API_KEY')
    APIToken = os.environ.get('TRELLO_API_TOKEN')

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

    for lists in jsonResponse: 
        lists_ids.append({'id': lists['id'], 'name': lists['name']})
        for card in lists['cards']:
            newitem = Item.from_trello_card(card,lists)
            items.append(newitem)

    return items

#def add_item(title,BOARD_ID,APIKey,APIToken):
def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item,BOARD_ID,APIKey,APIToken.

    Returns:
        item: The saved item.
    """

    #BOARD_ID = os.environ.get('TRELLO_BOARD_ID')
    #APIKey   = os.environ.get('TRELLO_API_KEY')
    #APIToken = os.environ.get('TRELLO_API_TOKEN')

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

    return None



#def delete_item(Selected_item,BOARD_ID,APIKey,APIToken):
def delete_item(Selected_item):
    """
    delete card using it's Selected_item, BOARD_ID, APIKey, APIToken.

    Args:
        The Trello card's Selected_item, BOARD_ID,APIKEY,APIToken.

    Returns:
        Nothing.
    """

    #BOARD_ID = os.environ.get('TRELLO_BOARD_ID')
    #APIKey   = os.environ.get('TRELLO_API_KEY')
    #APIToken = os.environ.get('TRELLO_API_TOKEN')

    query = {   
        'key': APIKey,
        'token': APIToken
    }

    url = "https://api.trello.com/1/cards/" + Selected_item
    response = requests.request("DELETE",url,params=query)

    return None

#def completed_item(Selected_item,BOARD_ID,APIKey,APIToken):
def completed_item(Selected_item):
    """
    completed card using it's shortLink and Done lists idList.

    Args:
        The Trello card's items id, BOARD_ID, APIKEY, APIToken.

    Returns:
        Nothing.
    """

    #BOARD_ID = os.environ.get('TRELLO_BOARD_ID')
    #APIKey   = os.environ.get('TRELLO_API_KEY')
    #APIToken = os.environ.get('TRELLO_API_TOKEN')

    for Done_idList in lists_ids:
        if Done_idList['name'] == 'Done':
            break

    query = {
        'idList':  Done_idList['id'],   
        'key': APIKey,
        'token': APIToken
    }

    url = "https://api.trello.com/1/cards/" + Selected_item
    response = requests.request("PUT",url,params=query)

    return None

#def not_started_item(Selected_item,BOARD_ID,APIKey,APIToken):
def not_started_item(Selected_item):
    """
    switch card to not started status using it's shortLink and Done lists idList.

    Args:
        The Trello card's items id, BOARD_ID, APIKEY, APIToken.

    Returns:
        Nothing.
    """

    #BOARD_ID = os.environ.get('TRELLO_BOARD_ID')
    #APIKey   = os.environ.get('TRELLO_API_KEY')
    #APIToken = os.environ.get('TRELLO_API_TOKEN')

    for Done_idList in lists_ids:
        if Done_idList['name'] == 'To Do':
            break

    query = {
        'idList':  Done_idList['id'],   
        'key': APIKey,
        'token': APIToken
    }

    url = "https://api.trello.com/1/cards/" + Selected_item
    response = requests.request("PUT",url,params=query)

    return None