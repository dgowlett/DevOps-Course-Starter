from todo_app.data.view_model import ViewModel
from todo_app.data.Item_class import Item

def test_done_items_property_only_returns_the_done_items():
    # Arrange
    items = [
        Item('0','0','test1','/test1','Done'), # Done Item 
        Item('1','1','test2','/test2','To Do')  # Todo Item 
    ]
    view_model = ViewModel(items)

    # Act
    returned_done_items = view_model.done_items

    # Assert
    assert len(returned_done_items) == 1
    done_item = returned_done_items[0]
    assert done_item.status == "Done"

def test_todo_items_property_only_returns_the_todo_items():
    # Arrange 2
    items = [
        Item('0','0','test1','/test1','Done'), # Done Item 
        Item('1','1','test2','/test2','To Do')  # Todo Item 
    ]
    view_model = ViewModel(items)
    
    # Act 2
    returned_todo_items = view_model.todo_items

    # Assert 2
    assert len(returned_todo_items) == 1
    todo_item = returned_todo_items[0]
    assert todo_item.status == "To Do"