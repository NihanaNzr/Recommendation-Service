import pytest
from fastapi.testclient import TestClient
from app.main import app  

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Recommendation Service"}
# Test if the /recommendations endpoint works and returns a status code of 200
def test_get_recommendations():
    response = client.get("/recommendations?category=Shirts&price_min=20&price_max=30&size=M&color=Blue&rating_min=4.0&sort_by=price&sort_order=asc&page=1&page_size=10")
    assert response.status_code == 200
    assert "items" in response.json()

def test_post_events():
    # Test if the /events endpoint works
    event_data = {
        "user_id": "user123",
        "item_id": "item_1",
        "event_type": "click"
    }
    response = client.post("/events", json=event_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Event recorded successfully"}
