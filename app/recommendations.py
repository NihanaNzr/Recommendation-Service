from typing import List
from app.models import FashionItem, UserEvent

def filter_items(items: List[FashionItem], filters: dict) -> List[FashionItem]:
    filtered = items
    if filters.get("category"):
        filtered = [item for item in filtered if item.category == filters["category"]]
    if filters.get("price_min") is not None:
        filtered = [item for item in filtered if item.price >= filters["price_min"]]
    if filters.get("price_max") is not None:
        filtered = [item for item in filtered if item.price <= filters["price_max"]]
    if filters.get("size"):
        filtered = [item for item in filtered if item.size == filters["size"]]
    if filters.get("color"):
        filtered = [item for item in filtered if item.color == filters["color"]]
    if filters.get("rating_min") is not None:
        filtered = [item for item in filtered if item.rating >= filters["rating_min"]]
    return filtered

def sort_items(items: List[FashionItem], sort_by: str, sort_order: str) -> List[FashionItem]:
    reverse = sort_order == "desc"
    return sorted(items, key=lambda x: getattr(x, sort_by, "id"), reverse=reverse)

def paginate_items(items: List[FashionItem], page: int, page_size: int) -> List[FashionItem]:
    start = (page - 1) * page_size
    return items[start:start + page_size]
