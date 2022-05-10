from flask import session
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
        'token': APIToken
    }

    print(query)
    url = "https://api.trello.com/1/boards/" + BOARD_ID + "/cards"
    print(url)
    response = requests.request("GET",url,params=query)

    jsonResponse = response.json()
    items=[]
    #get lists To-do, doing, done

    print(jsonResponse)
    for dataline in jsonResponse:
        print(dataline['id'])
        print(dataline['name'])
        print(dataline['shortLink'])
        getitem = {'id': dataline['id'], 'title': dataline['name'], 'status': dataline['shortLink']}
        items.append(getitem)
        #for key, value in dataline.items():
        #    if key == 'name':
        #        print(key, ":", value)
        #    elif key == 'id':
        #        print(key, ":", value)

    print(items)
    #return session.get('items', _DEFAULT_ITEMS.copy())
    return items
    #return next((item for item in dataline.items() if item['name'] == 'name', None)
