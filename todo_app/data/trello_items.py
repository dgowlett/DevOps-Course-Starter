# Trello card actions
#
import requests
import json
from todo_app.data.Item_class import Item

lists_ids=[]

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
            newitem = Item.from_trello_card(card,lists)
            #newitem = {'id': id_number, 'title': new_items.name, 'status': new_items.status, 'shortLink': new_items.shortLink, 'idList': new_items.idList}
            items.append(newitem)
            #id_number += 1

    return items

def add_item(title,BOARD_ID,APIKey,APIToken):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item,BOARD_ID,APIKey,APIToken.

    Returns:
        item: The saved item.
    """
    #####items = get_items(BOARD_ID,APIKey,APIToken)

    # Determine the ID for the item based on that of the previously added item
    #####id = items[-1]['id'] + 1 if items else 0

    #####item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    #####items.append(item)

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




def delete_item(Selected_item,BOARD_ID,APIKey,APIToken):
    """
    delete card using it's Selected_item, BOARD_ID, APIKey, APIToken.

    Args:
        The Trello card's Selected_item, BOARD_ID,APIKEY,APIToken.

    Returns:
        Nothing.
    """

    query = {   
        'key': APIKey,
        'token': APIToken
    }

    url = "https://api.trello.com/1/cards/" + Selected_item
    response = requests.request("DELETE",url,params=query)

    return None


def completed_item(Selected_item,BOARD_ID,APIKey,APIToken):
    """
    completed card using it's shortLink and Done lists idList.

    Args:
        The Trello card's items id, BOARD_ID, APIKEY, APIToken.

    Returns:
        Nothing.
    """

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
    #break

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

    #for findSelection in items:
        #if findSelection['id'] == int(Selected_item):
            #shortLink=findSelection['shortLink']
    url = "https://api.trello.com/1/cards/" + Selected_item
    response = requests.request("PUT",url,params=query)
            #break

    return None