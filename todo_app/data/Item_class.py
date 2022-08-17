class Item: 
    def __init__(self, idList, id, name, shortLink, status = 'To Do'): 
        self.idList = idList 
        self.id = id
        self.name = name 
        self.shortLink = shortLink
        self.status = status
   
    @classmethod 
    def from_trello_card(cls, card, list): 
        return cls(card['idList'], card['id'],card['name'], card['shortLink'], list['name'])