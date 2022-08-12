class Item: 
    def __init__(self, idList, name, shortLink, status = 'To Do'): 
        self.idList = idList 
        self.name = name 
        self.shortLink = shortLink
        self.status = status
   
    @classmethod 
    def from_trello_card(cls, card, list): 
        return cls(card['idList'], card['name'], card['shortLink'], list['name'])