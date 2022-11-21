from todo_app.data.Item_class import Item

class ViewModel:
    def __init__(self, items: list[Item]):
        self._items = items
 
    @property
    def items(self) -> list[Item]:
        return self._items
        
    @property
    def todo_items(self) -> list[Item]:
        return []

    @property
    def done_items(self) -> list[Item]:
        return []