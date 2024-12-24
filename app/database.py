from faker import Faker
import random
from app.models import FashionItem, UserEvent

fake = Faker()

# Generate mock fashion item data
def generate_fashion_items(num_items=100):
    categories = ["Shirts", "Pants", "Dresses", "Accessories", "Shoes"]
    sizes = ["S", "M", "L", "XL"]
    colors = ["Red", "Blue", "Black", "White", "Green"]
    
    return [
        FashionItem(
            id=f"item_{i}",
            name=f"{fake.word().capitalize()} {random.choice(categories)}",
            category=random.choice(categories),
            price=random.randint(20, 2000),
            size=random.choice(sizes),
            color=random.choice(colors),
            rating=round(random.uniform(1.0, 5.0), 1)
        )
        for i in range(1, num_items + 1)
    ]

# Generate mock user events
def generate_user_events(num_events=50):
    event_types = ["view", "like", "purchase"]
    return [
        UserEvent(
            user_id=f"user_{random.randint(1, 20)}",
            item_id=f"item_{random.randint(1, 100)}",
            event_type=random.choice(event_types)
        )
        for _ in range(num_events)
    ]

# Mock dataset
fashion_items = generate_fashion_items()
user_events = generate_user_events()
