from pydantic import BaseModel
from typing import Optional, List

class FashionItem(BaseModel):
    id: str
    name: str
    category: str
    price: float
    size: str
    color: str
    rating: float

class UserEvent(BaseModel):
    user_id: str
    item_id: str
    event_type: str

class RecommendationQuery(BaseModel):
    category: Optional[str]
    price_min: Optional[float]
    price_max: Optional[float]
    size: Optional[str]
    color: Optional[str]
    rating_min: Optional[float]
    sort_by: Optional[str]
    sort_order: Optional[str]
    page: Optional[int]
    page_size: Optional[int]
