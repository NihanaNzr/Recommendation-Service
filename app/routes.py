from fastapi import APIRouter, HTTPException, Query
from app.models import FashionItem, UserEvent
from app.database import fashion_items, user_events
from app.recommendations import filter_items, sort_items, paginate_items

router = APIRouter()

@router.get("/recommendations")
def get_recommendations(category: str = None, price_min: float = None, price_max: float = None,
                        size: str = None, color: str = None, rating_min: float = None,
                        sort_by: str = "price", sort_order: str = "asc",
                        page: int = 1, page_size: int = 10):
    filters = {
        "category": category,
        "price_min": price_min,
        "price_max": price_max,
        "size": size,
        "color": color,
        "rating_min": rating_min,
    }
    items = filter_items(fashion_items, filters)
    items = sort_items(items, sort_by, sort_order)
    items = paginate_items(items, page, page_size)
    return {"items": items}

@router.post("/events")
def post_event(event: UserEvent):
    if not any(item.id == event.item_id for item in fashion_items):
        raise HTTPException(status_code=404, detail="Item not found")
    user_events.append(event)
    return {"message": "Event recorded successfully"}
