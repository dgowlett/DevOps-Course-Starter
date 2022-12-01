from todo_app.data.item import Item
from todo_app.data.view_model import ViewModel

def test_done_items_property_only_returns_items_with_done_status():
    # Arrange
    items = [
        Item("1", "Cleaning Floor", "To Do"),
        Item("2", "Washing up", "Done")
    ]
    view_model = ViewModel(items)

    # Act
    returned_items = view_model.done_items

    # Assert
    assert len(returned_items) == 1

    single_item = returned_items[0]

    assert single_item.status == "Done"