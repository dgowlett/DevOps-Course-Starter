from todo_app.data.item import Item

class ViewModel:
    def __init__(self, items: list[Item]):
        self._items = items
 
    @property
    def items(self) -> list[Item]:
        return self._items
        
    @property
    def todo_items(self) -> list[Item]:
        todo=[]
        for entires in self._items: 
            if entires.status == "To Do":
                todo.append(entires)
        # status is Todo
        return todo

    @property
    def done_items(self) -> list[Item]:
        done=[]
        for entires in self._items: 
            if entires.status == "Done":
                done.append(entires)
        # status is completed 
        return done