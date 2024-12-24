from app.database import fashion_items, user_events
from app.recommendations import filter_items, sort_items, paginate_items

def test_filter_items():
    filters = {"category": "Shirts", "color": "Blue"}
    result = filter_items(fashion_items, filters)
    assert all(item.category == "Shirts" and item.color == "Blue" for item in result)
    assert len(result) > 0  # Ensure at least one item matches


def test_sort_items():
    sorted_items = sort_items(fashion_items, "price", "asc")
    assert all(sorted_items[i].price <= sorted_items[i + 1].price for i in range(len(sorted_items) - 1))

    sorted_items_desc = sort_items(fashion_items, "price", "desc")
    assert all(sorted_items_desc[i].price >= sorted_items_desc[i + 1].price for i in range(len(sorted_items_desc) - 1))


def test_paginate_items():
    sorted_items = sort_items(fashion_items, "price", "asc")  # Explicitly sort by price
    paginated = paginate_items(sorted_items, page=1, page_size=10)
    assert len(paginated) == 10  # Should return 10 items
    assert paginated[0].price == sorted_items[0].price  # First item matches lowest price


def test_no_results_for_invalid_filter():
    filters = {"category": "NonexistentCategory", "color": "NonexistentColor"}
    result = filter_items(fashion_items, filters)
    assert len(result) == 0  # Ensure no items match the invalid filter


def test_combined_filter_and_pagination():
    filters = {"category": "Shirts", "color": "Blue"}
    filtered_items = filter_items(fashion_items, filters)
    paginated_items = paginate_items(filtered_items, page=1, page_size=5)
    assert len(paginated_items) <= 5  # Page size should be respected
    assert all(item.category == "Shirts" and item.color == "Blue" for item in paginated_items)

